from fastapi import APIRouter, Depends
from ..schemas.usuario import UsuarioResponse, UsuarioUpdate
from ..models.usuario import Usuario
from .auth import get_current_user_from_token

router = APIRouter(prefix="/users", tags=["users"])

# Obtiene el perfil del usuario actualmente autenticado
@router.get("/me", response_model=UsuarioResponse)
def get_obtener_perfil_actual(current_user: Usuario = Depends(get_current_user_from_token)):
   
    return current_user

# Actualiza el perfil del usuario actualmente autenticado
@router.put("/me", response_model=UsuarioUpdate)
def put_actualizar_perfil_actual(
    updated_user: UsuarioUpdate,
    current_user: Usuario = Depends(get_current_user_from_token)
):
    current_user.nombre_completo = updated_user.nombre_completo
    current_user.bio = updated_user.bio

    from ..db.database import SessionLocal
    db = SessionLocal()
    try:
        db.add(current_user)
        db.commit()
        db.refresh(current_user)
    finally:
        db.close()

    return current_user
