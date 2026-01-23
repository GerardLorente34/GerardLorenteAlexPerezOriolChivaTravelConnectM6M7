from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..db.deps import get_db
from ..models.viajero import Viaje
from ..models.usuario import Usuario
from ..utils.auth import get_current_user_from_token
from ..schemas.chat import ChatMessageResponse, SendMessageRequest
from ..crud.chat import get_mensajes_viaje, create_mensaje

router = APIRouter(prefix="/trips", tags=["chat"])


def _verificar_acceso_chat(viaje: Viaje, usuario: Usuario):
    if usuario not in viaje.participantes and viaje.creador_id != usuario.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes acceso a este chat"
        )


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
    
    # Obtener mensajes usando CRUD
    mensajes = get_mensajes_viaje(db, id)
    
    # Transformar a respuesta con username del autor
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
    
    # Crear mensaje usando CRUD
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