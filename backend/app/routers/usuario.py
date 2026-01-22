from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.usuario import UsuarioResponse, UsuarioUpdate
from ..models.usuario import Usuario
from ..db.deps import get_db
from ..utils.auth import get_current_user_from_token

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/me", response_model=UsuarioResponse)
def get_perfil_actual(
    current_user: Usuario = Depends(get_current_user_from_token)
):
    return current_user

@router.put("/me", response_model=UsuarioResponse)
def put_actualizar_perfil_actual(
    updated_user: UsuarioUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    if updated_user.nombre_completo is not None:
        current_user.nombre_completo = updated_user.nombre_completo
    if updated_user.bio is not None:
        current_user.bio = updated_user.bio

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
