from sqlalchemy.orm import Session, joinedload
from ..models.usuario import Usuario
from ..schemas.usuario import UsuarioUpdate, UsuarioCreate
from ..db.database import SessionLocal

def get_usuarios(db: Session) -> list[Usuario]:
    return db.query(Usuario).all()

def get_usuario(db: Session, usuario_id: int) -> Usuario:
    return (
        db.query(Usuario)
        .options(joinedload(Usuario.viajes_creados), joinedload(Usuario.viajes_inscritos))
        .filter(Usuario.id == usuario_id)
        .first()
    )

def create_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    db_usuario = Usuario(
        username=usuario.username,
        email=usuario.email,
        hashed_password=usuario.hashed_password,
        nombre_completo=usuario.nombre_completo,
        rol=usuario.rol,
        bio=usuario.bio
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario_update: UsuarioUpdate) -> Usuario | None:
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return None

    data = usuario_update.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_usuario, field, value)

    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int) -> bool:
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        return False

    db.delete(db_usuario)
    db.commit()
    return True


