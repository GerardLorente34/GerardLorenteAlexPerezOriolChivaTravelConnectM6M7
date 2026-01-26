from fastapi import APIRouter, Depends, HTTPException, status, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session
from typing import List
import jwt

from ..db.deps import get_db
from ..models.viajero import Viaje
from ..models.usuario import Usuario
from ..utils.auth import get_current_user_from_token, SECRET_KEY, ALGORITHM
from ..schemas.chat import ChatMessageResponse, SendMessageRequest
from ..crud.chat import get_mensajes_viaje, create_mensaje
from ..utils.chat import manager

router = APIRouter(prefix="/trips", tags=["chat"])


def _verificar_acceso_chat(viaje: Viaje, usuario: Usuario):
    if usuario not in viaje.participantes and viaje.creador_id != usuario.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes acceso a este chat"
        )


async def get_user_from_token(token: str, db: Session) -> Usuario:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            return None
        return db.query(Usuario).filter(Usuario.username == username).first()
    except Exception:
        return None


@router.get("/{id}/chat", response_model=List[ChatMessageResponse])
def get_trip_chat_messages(
    id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viaje = db.query(Viaje).filter(Viaje.id == id).first()
    if not viaje:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Viaje no encontrado"
        )
    
    _verificar_acceso_chat(viaje, current_user)
    
    mensajes = get_mensajes_viaje(db, id)
    
    response = []
    for msg in mensajes:
        response.append(ChatMessageResponse(
            id=msg.id,
            viaje_id=msg.viaje_id,
            autor_id=msg.autor_id,
            autor_username=msg.autor.username,
            contenido=msg.contenido,
            timestamp=msg.timestamp
        ))
    
    return response


@router.post("/{id}/chat/send", response_model=ChatMessageResponse, status_code=status.HTTP_201_CREATED)
def send_chat_message(
    id: int,
    message: SendMessageRequest,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viaje = db.query(Viaje).filter(Viaje.id == id).first()
    if not viaje:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Viaje no encontrado"
        )
    
    _verificar_acceso_chat(viaje, current_user)
    
    nuevo_mensaje, error = create_mensaje(db, id, current_user.id, message.contenido)
    
    if error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )
    
    return ChatMessageResponse(
        id=nuevo_mensaje.id,
        viaje_id=nuevo_mensaje.viaje_id,
        autor_id=nuevo_mensaje.autor_id,
        autor_username=current_user.username,
        contenido=nuevo_mensaje.contenido,
        timestamp=nuevo_mensaje.timestamp
    )


@router.websocket("/ws/{trip_id}/chat")
async def websocket_chat_endpoint(
    websocket: WebSocket,
    trip_id: int,
    token: str = Query(...),
    db: Session = Depends(get_db)
):
    # Verificar autenticación
    user = await get_user_from_token(token, db)
    if not user:
        await websocket.close(code=1008)  # Policy Violation
        return
    
    # Verificar que el viaje existe
    viaje = db.query(Viaje).filter(Viaje.id == trip_id).first()
    if not viaje:
        await websocket.close(code=1008)
        return
    
    # Verificar acceso al chat
    if user not in viaje.participantes and viaje.creador_id != user.id:
        await websocket.close(code=1008)
        return
    
    # Conectar usuario
    await manager.connect(websocket, trip_id)
    
    try:
        while True:
            # Recibir mensaje del cliente
            data = await websocket.receive_json()
            contenido = data.get("contenido", "").strip()
            
            if not contenido:
                continue
            
            # Guardar mensaje en la base de datos
            nuevo_mensaje, error = create_mensaje(db, trip_id, user.id, contenido)
            
            if error:
                await websocket.send_json({
                    "error": error
                })
                continue
            
            # Broadcast del mensaje a todos los conectados
            message_data = {
                "id": nuevo_mensaje.id,
                "viaje_id": nuevo_mensaje.viaje_id,
                "autor_id": nuevo_mensaje.autor_id,
                "autor_username": user.username,
                "contenido": nuevo_mensaje.contenido,
                "timestamp": nuevo_mensaje.timestamp.isoformat()
            }
            
            await manager.broadcast(trip_id, message_data)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket, trip_id)
    except Exception as e:
        manager.disconnect(websocket, trip_id)
        print(f"Error en WebSocket: {e}")