from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from typing import List, Optional, Tuple

from ..models.mensajesXat import MissatgeXat
from ..models.viajero import Viaje
from ..models.usuario import Usuario


def get_mensajes_viaje(db: Session, viaje_id: int) -> List[MissatgeXat]:
    return (
        db.query(MissatgeXat)
        .options(joinedload(MissatgeXat.autor))  # Cargar relación con autor
        .filter(MissatgeXat.viaje_id == viaje_id)
        .order_by(MissatgeXat.timestamp.asc())
        .all()
    )


def create_mensaje(
    db: Session, 
    viaje_id: int, 
    autor_id: int, 
    contenido: str
) -> Tuple[Optional[MissatgeXat], Optional[str]]:
    if not contenido or not contenido.strip():
        return None, "El mensaje no puede estar vacío"
    
    nuevo_mensaje = MissatgeXat(
        viaje_id=viaje_id,
        autor_id=autor_id,
        contenido=contenido.strip(),
        timestamp=datetime.utcnow()
    )
    
    db.add(nuevo_mensaje)
    db.commit()
    db.refresh(nuevo_mensaje)
    
    # Cargar relación con autor para retornar objeto completo
    db.refresh(nuevo_mensaje, ['autor'])
    
    return nuevo_mensaje, None


def delete_mensaje(db: Session, mensaje_id: int, usuario_id: int) -> Tuple[bool, Optional[str]]:
    mensaje = db.query(MissatgeXat).filter(MissatgeXat.id == mensaje_id).first()
    
    if not mensaje:
        return False, "Mensaje no encontrado"
    
    if mensaje.autor_id != usuario_id:
        return False, "No puedes eliminar este mensaje"
    
    db.delete(mensaje)
    db.commit()
    return True, None