from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Enum as SQLEnum, Table
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum

# Enum para el estado del viaje
class EstadoViaje(str, enum.Enum):
    PLANIFICADO = "planificado"
    ACTIVO = "activo"
    COMPLETADO = "completado"
    CANCELADO = "cancelado"

# Tabla de asociación para la relación ManyToMany entre Viaje y Usuario (participantes)
viajes_participantes = Table(
    'viajes_participantes',
    Base.metadata,
    Column('viaje_id', Integer, ForeignKey('viajes.id'), primary_key=True),
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True)
)

class Viaje(Base):
    __tablename__ = "viajes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    destino = Column(String(200), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    descripcion = Column(Text, nullable=True)
    maximo_participantes = Column(Integer, nullable=False)
    total_participantes = Column(Integer, default=0, nullable=False)
    estado = Column(SQLEnum(EstadoViaje), default=EstadoViaje.PLANIFICADO, nullable=False)
    
    # ForeignKey: creador del viaje
    creador_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    
    # Relaciones
    creador = relationship("Usuario", foreign_keys=[creador_id], back_populates="viajes_creados")
    participantes = relationship("Usuario", secondary=viajes_participantes, back_populates="viajes_inscritos")

