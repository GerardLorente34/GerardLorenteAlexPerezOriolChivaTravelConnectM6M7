from sqlalchemy.orm import Session, joinedload
from ..models.usuario import Usuario, RolUsuario
from ..schemas.viajero_viaje import ViajeroCreate, ViajeroUpdate

def get_viajeros(db: Session):
    return db.query(Usuario).filter(Usuario.rol == RolUsuario.VIAJERO).all()

def get_viajero(db: Session, viajero_id: int):
    return (
        db.query(Usuario)
        .options(joinedload(Usuario.viajes_inscritos))
        .filter(Usuario.id == viajero_id, Usuario.rol == RolUsuario.VIAJERO)
        .first()
    )

def create_viajero(db: Session, viajero: ViajeroCreate):
    db_viajero = Usuario(
        username=viajero.username,
        email=viajero.email,
        hashed_password="",  # TODO: generar hash al registrar
        nombre_completo=viajero.nombre_completo,
        rol=RolUsuario.VIAJERO,
        bio=viajero.bio,
    )
    db.add(db_viajero)
    db.commit()
    db.refresh(db_viajero)
    return db_viajero

def update_viajero(db: Session, viajero_id: int, viajero_in: ViajeroUpdate):
    db_viajero = db.query(Usuario).filter(
        Usuario.id == viajero_id, Usuario.rol == RolUsuario.VIAJERO
    ).first()
    if not db_viajero:
        return None
    if viajero_in.nombre_completo is not None:
        db_viajero.nombre_completo = viajero_in.nombre_completo
    if viajero_in.bio is not None:
        db_viajero.bio = viajero_in.bio
    db.commit()
    db.refresh(db_viajero)
    return db_viajero

def delete_viajero(db: Session, viajero_id: int):
    db_viajero = get_viajero(db, viajero_id)
    if db_viajero:
        db.delete(db_viajero)
        db.commit()
        return True
    return False
