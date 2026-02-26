from sqlalchemy.orm import Session, joinedload
from ..models.viajero import Viaje, EstadoViaje
from ..models.usuario import Usuario
from ..schemas.viajero_viaje import ViajeCreate, ViajeUpdate

def get_viajes_disponibles(db: Session):
    return db.query(Viaje).filter(Viaje.estado == EstadoViaje.PLANIFICADO).all()

def get_viaje(db: Session, viaje_id: int):
    return (
        db.query(Viaje)
        .options(joinedload(Viaje.participantes))
        .filter(Viaje.id == viaje_id)
        .first()
    )

def create_viaje(db: Session, viaje: ViajeCreate, creador_id: int):
    db_viaje = Viaje(
        nombre=viaje.nombre,
        destino=viaje.destino,
        fecha_inicio=viaje.fecha_inicio,
        fecha_fin=viaje.fecha_fin,
        descripcion=viaje.descripcion,
        maximo_participantes=viaje.maximo_participantes,
        creador_id=creador_id,
        estado=EstadoViaje.PLANIFICADO
    )
    db.add(db_viaje)
    db.commit()
    db.refresh(db_viaje)
    return db_viaje

def update_viaje(db: Session, viaje_id: int, viaje: ViajeUpdate):
    db_viaje = db.query(Viaje).filter(Viaje.id == viaje_id).first()
    if not db_viaje:
        return None, "Viaje no encontrado"

    data = viaje.dict(exclude_unset=True)
    
    if "estado" in data:
        try:
            data["estado"] = EstadoViaje(data["estado"])
        except ValueError:
            return None, "Estado inválido"
        
    nuevo_max = data.get("maximo_participantes")
    if nuevo_max is not None and nuevo_max < db_viaje.total_participantes:
        return None, "No se puede reducir el máximo por debajo de los inscritos"

    for field, value in data.items():
        setattr(db_viaje, field, value)

    db.commit()
    db.refresh(db_viaje)
    return db_viaje, None

def inscribir_viajero(db: Session, viaje_id: int, usuario_id: int):
    viaje = (
        db.query(Viaje)
        .options(joinedload(Viaje.participantes))
        .filter(Viaje.id == viaje_id)
        .first()
    )
    if not viaje:
        return None, "Viaje no encontrado"
    
    if viaje.total_participantes >= viaje.maximo_participantes:
        return None, "Viaje completo"
    
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None, "Usuario no encontrado"
    
    if usuario in viaje.participantes:
        return None, "Ya estás inscrito en este viaje"
    
    viaje.participantes.append(usuario)
    viaje.total_participantes += 1
    db.commit()
    db.refresh(viaje)
    return viaje, None


def desinscribir_viajero(db: Session, viaje_id: int, usuario_id: int):
    viaje = (
        db.query(Viaje)
        .options(joinedload(Viaje.participantes))
        .filter(Viaje.id == viaje_id)
        .first()
    )
    if not viaje:
        return None, "Viaje no encontrado"
    
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        return None, "Usuario no encontrado"
    
    if usuario not in viaje.participantes:
        return None, "No estás inscrito en este viaje"
    
    viaje.participantes.remove(usuario)
    viaje.total_participantes -= 1
    db.commit()
    db.refresh(viaje)
    return viaje, None

def delete_viaje(db: Session, viaje_id: int):
    db_viaje = db.query(Viaje).filter(Viaje.id == viaje_id).first()
    if not db_viaje:
        return False, "Viaje no encontrado"

    db_viaje.participantes.clear()  # evita restes a la taula N:N
    db.commit()

    db.delete(db_viaje)
    db.commit()
    return True, None
