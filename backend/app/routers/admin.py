from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from ..schemas.usuario import UsuarioResponse
from ..schemas.peticionPromocion import PeticionPromocionResponse
from ..db.deps import get_db
from ..models.usuario import Usuario
from ..models.peticionPromocion import PeticionPromocion
from ..utils.auth import get_current_user

router = APIRouter(prefix="/admin", tags=["admin"])

class RoleUpdate(BaseModel):
    rol: str # "viajero", "creador", "admin"

class PromotionDecision(BaseModel):
    estado: str # "aprobado" o "rechazado"

def check_admin(user: Usuario):
    if user.rol !="admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario no autorizado, solo administradores")


@router.get("/users", response_model=List[UsuarioResponse])
def list_users(current_user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):

    check_admin(current_user)
    return db.query(Usuario).all()

@router.put("/users/{user_id}/promote", response_model=UsuarioResponse)
def change_user_role(user_id: int, payload: RoleUpdate, current_user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):

    check_admin(current_user)

    if payload.rol not in ("viajero", "creador", "admin"):
        raise HTTPException(status_code=400, detail="Rol inválido")
    
    user = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.rol = payload.rol
    db.commit()
    db.refresh(user)
    return user

@router.get("/promotions", response_model=List[PeticionPromocionResponse])
def lista_promoticiones(current_user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    check_admin(current_user)
    return db.query(PeticionPromocion).filter(PeticionPromocion.estado == "Pendiente").all()


@router.put("/promotions/{promotion_id}")
def decidir_promocion(promotion_id: int, payload: PromotionDecision, current_user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):

    check_admin(current_user)

    if payload.estado not in ("Aprobado", "Rechazado"):
        raise HTTPException(status_code=400, detail="Estado inválido")
    
    req = db.query(PeticionPromocion).filter(PeticionPromocion.id == promotion_id).first()

    if not req:
        raise HTTPException(status_code=404, detail="Petición no encontrada")
    
    if req.estado != "Pendiente":
        raise HTTPException(status_code=400, detail="Petición ya gestionada")
    
    req.estado = payload.estado

    
    if payload.estado == "Aprobado":
        user = db.query(Usuario).filter(Usuario.id == req.usuario_solicitante_id).first()

        if not user:
            raise HTTPException(status_code=404, detail="Usuario solicitante no encontrado")
        
        if user.rol == "viajero":
            user.rol = "creador"
    

    
    db.commit()
    db.refresh(req)
    return req