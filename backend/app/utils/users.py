from fastapi import APIRouter, Depends
from ..schemas.usuario import UsuarioResponse
from ..models.usuario import Usuario
from .auth import get_current_user_from_token

router = APIRouter(prefix="/users", tags=["users"])

# Obtiene el perfil del usuario actualmente autenticado
@router.get("/me", response_model=UsuarioResponse)
def get_obtener_perfil_actual(current_user: Usuario = Depends(get_current_user_from_token)):
   
    return current_user