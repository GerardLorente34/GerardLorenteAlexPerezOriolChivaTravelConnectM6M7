from sqlalchemy.orm import Session
from ..models.peticionPromocion import PeticionPromocion, EstadoPromocion

def get_peticiones_pendientes(db: Session):
    return db.query(PeticionPromocion).filter(
        PeticionPromocion.estado == EstadoPromocion.Pendiente
    ).all()

def get_peticion(db: Session, peticion_id: int):
    return db.query(PeticionPromocion).filter(PeticionPromocion.id == peticion_id).first()

def create_peticion(db: Session, usuario_id: int, mensaje: str):
    # Verificar si ya tiene una petición pendiente
    existing = db.query(PeticionPromocion).filter(
        PeticionPromocion.usuario_solicitante_id == usuario_id,
        PeticionPromocion.estado == EstadoPromocion.Pendiente
    ).first()
    
    if existing:
        return None, "Ya tienes una petición pendiente"
    
    nueva_peticion = PeticionPromocion(
        usuario_solicitante_id=usuario_id,
        mensaje_peticion=mensaje,
        estado=EstadoPromocion.Pendiente
    )
    
    db.add(nueva_peticion)
    db.commit()
    db.refresh(nueva_peticion)
    return nueva_peticion, None

def aprobar_peticion(db: Session, peticion_id: int):
    peticion = db.query(PeticionPromocion).filter(PeticionPromocion.id == peticion_id).first()
    if not peticion:
        return None
    
    peticion.estado = EstadoPromocion.Aprobado
    db.commit()
    db.refresh(peticion)
    return peticion

def rechazar_peticion(db: Session, peticion_id: int):
    peticion = db.query(PeticionPromocion).filter(PeticionPromocion.id == peticion_id).first()
    if not peticion:
        return None
    
    peticion.estado = EstadoPromocion.Rechazado
    db.commit()
    db.refresh(peticion)
    return peticion
