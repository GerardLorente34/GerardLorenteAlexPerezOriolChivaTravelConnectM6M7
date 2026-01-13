from sqlalchemy.orm import Session, joinedload
from ..models.viajero import Viajero
from ..models.viajero_viaje import ViajeroViaje
from ..schemas.viajero_viaje import ViajeroResponse, ViajeroUpdate

def get_viajeros(db: Session):
    return db.query(Viajero).all()

def get_viajero(db: Session, viajero_id: int):
    return db.query(Viajero).options(
        joinedload(Viajero.viajes).joinedload(ViajeroViaje.viaje)
    ).filter(Viajero.id == viajero_id).first()

def create_viajero(db: Session, viajero: ViajeroResponse):
    db_viajero = Viajero(nombre=viajero.nombre, email=viajero.email)
    db.add(db_viajero)
    db.commit()
    db.refresh(db_viajero)
    return db_viajero

def update_viajero(db: Session, viajero_id: int, viajero_in: ViajeroUpdate):
    # buscamos el viajero
    db_viajero = db.query(Viajero).filter(Viajero.id == viajero_id).first()

    if not db_viajero:
        return None
    
    # actualizamos solo los campos que tienen valor
    if viajero_in.nombre is not None:
        db_viajero.nombre = viajero_in.nombre
    if viajero_in.email is not None:
        db_viajero.email = viajero_in.email

    db.commit()
    db.refresh(db_viajero)
    return db_viajero

def delete_alumno(db: Session, viajero_id: int):
    db_viajero = get_viajero(db, viajero_id)
    if db_viajero:
        db.delete(db_viajero)
        db.commit()
        return True
    return False
