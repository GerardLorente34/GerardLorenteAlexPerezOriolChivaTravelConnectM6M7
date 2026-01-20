from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..db.deps import get_db
from ..crud.peticion import create_peticion
from ..utils.auth import get_current_user_from_token
from ..models.usuario import Usuario

router = APIRouter(tags=["promocion"])

class PromoteRequest(BaseModel):
    mensaje_peticion: str

class PromoteResponse(BaseModel):
    id: int
    usuario_solicitante_id: int
    mensaje_peticion: str
    estado: str

    class Config:
        from_attributes = True

@router.post("/promote-request", response_model=PromoteResponse)
def create_promote_request(
    request: PromoteRequest,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    peticion, error = create_peticion(db, current_user.id, request.mensaje_peticion)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return peticion
