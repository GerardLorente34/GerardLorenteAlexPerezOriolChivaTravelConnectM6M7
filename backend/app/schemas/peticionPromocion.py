from pydantic import BaseModel
from typing import Optional

class PeticionPromocionResponse(BaseModel):
    id: int
    usuario_solicitante_id: int
    mensaje_peticion: Optional[str] = None
    estado: str

    class Config:
        from_attributes = True

