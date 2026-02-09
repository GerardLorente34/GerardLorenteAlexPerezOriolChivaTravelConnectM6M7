from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr

from ..db.database import SessionLocal
from ..models.usuario import RolUsuario, Usuario
from ..utils.auth import hash_password, authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

class RegisterIn(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: str | None = None

@router.post("/register")
def register(data: RegisterIn):
    db = SessionLocal()
    try:
        if db.query(Usuario).filter(Usuario.username == data.username).first():
            raise HTTPException(status_code=400, detail="El username ya existe")
        
        if db.query(Usuario).filter(Usuario.email == data.email).first():
            raise HTTPException(status_code=400, detail="El email ya existe")
        
        user = Usuario(
            username=data.username,
            email=data.email,
            nombre_completo=data.full_name or data.username,
            hashed_password=hash_password(data.password),
            rol=RolUsuario.VIAJERO,  # por defecto
            bio="",
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return{
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "full_name": user.nombre_completo,
            "rol": user.rol,
            "bio": user.bio
        }
    finally:
        db.close()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user.username, "role": user.rol}
    )

    return { "access_token": access_token,
            "token_type": "bearer",
            "user_id": user.id,
            "rol": user.rol 
            }