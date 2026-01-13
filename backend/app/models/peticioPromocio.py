from sqlalchemy import Column, Integer, String, Enum as SQLEnum, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum

# Enum para el estado de la petición de promoción
class EstatPromocio(str, enum.Enum):
    Pendent = "pendent"
    Aprovat = "aprovat"
    Rebutjat = "rebutjat"


class PeticioPromocio(Base):
    __tablename__ = "peticions_promocio"
    
    id = Column(Integer, primary_key=True, index=True)
    usuari_solicitant_id = Column(Integer, ForeignKey("usuaris.id"), nullable=False)
    missatge_peticio = Column(Text, nullable=False)
    estat = Column(SQLEnum(EstatPromocio), default=EstatPromocio.Pendent, nullable=False)
    
    # Relación con Usuari
    usuari_solicitant = relationship("Usuari", backref="peticions_promocio")