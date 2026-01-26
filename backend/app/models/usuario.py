from sqlalchemy import Column, Integer, String, Enum as SQLEnum, Text
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum

class RolUsuario(str, enum.Enum):
    VIAJERO = "viajero"
    CREADOR = "creador"
    ADMINISTRADOR = "administrador"

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    nombre_completo = Column(String(100), nullable=False)
    rol = Column(SQLEnum(RolUsuario), default=RolUsuario.VIAJERO, nullable=False)
    bio = Column(Text, nullable=True)
    
    # Relaciones con Viaje
    viajes_creados = relationship("Viaje", foreign_keys="Viaje.creador_id", back_populates="creador")
    viajes_inscritos = relationship("Viaje", secondary="viajes_participantes", back_populates="participantes")

