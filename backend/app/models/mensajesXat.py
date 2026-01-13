from sqlalchemy import Column, Integer, Enum as SQLEnum, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db.database import Base


class MissatgeXat(Base):
    __tablename__ = "mensajes"
    
    id = Column(Integer, primary_key=True, index=True)
    viaje_id = Column(Integer, ForeignKey("viajes.id"), nullable=False)
    autor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    contenido = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    # Relación con Viaje
    viaje = relationship("Viaje", backref="mensajes")
    # Relación con Usuario
    autor = relationship("Usuario", backref="mensajes")