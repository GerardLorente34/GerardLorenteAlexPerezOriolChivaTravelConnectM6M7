from sqlalchemy import Column, Integer, String, Enum as SQLEnum, Text
from ..db.database import Base
import enum

class RolUsuari(str, enum.Enum):
    VIATGER = "viatger"
    CREADOR = "creador"
    ADMINISTRADOR = "administrador"

class Usuari(Base):
    __tablename__ = "usuaris"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    rol = Column(SQLEnum(RolUsuari), default=RolUsuari.VIATGER, nullable=False)
    bio = Column(Text, nullable=True)
    
   