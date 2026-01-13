from sqlalchemy import Column, Integer, Enum as SQLEnum, Text, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.models.peticionPromocion import EstadoPromocion
from ..db.database import Base
import enum

# Enum para el estado de la petición de promoción
class EstadoPromocion(str, enum.Enum):
    Pendiente = "pendiente"
    Aprobado = "aprobado"
    Rechazado = "rechazado"

class PeticionPromocion(Base):
    __tablename__ = "peticiones"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_solicitante_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    mensaje_peticion = Column(Text, nullable=False)
    estado = Column(SQLEnum(EstadoPromocion), default=EstadoPromocion.Pendiente, nullable=False)
    
    # Relación con Usuario
    usuario_solicitante = relationship("Usuario", backref="peticiones")