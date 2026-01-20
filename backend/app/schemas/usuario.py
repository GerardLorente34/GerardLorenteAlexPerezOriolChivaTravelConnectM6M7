from pydantic import BaseModel, EmailStr
from typing import Optional
from ..models.usuario import RolUsuario


class UsuarioUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    bio: Optional[str] = None


class UsuarioResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    nombre_completo: str
    rol: RolUsuario
    bio: Optional[str] = None

    class Config:
        from_attributes = True
