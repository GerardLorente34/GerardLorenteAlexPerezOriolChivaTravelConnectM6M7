from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Enum as SQLEnum, Table
from sqlalchemy.orm import relationship
from ..db.database import Base
import enum

# Enum para el estado del viaje
class EstatViatge(str, enum.Enum):
    PLANIFICANT = "planificant"
    ACTIU = "actiu"
    COMPLETAT = "completat"
    CANCELAT = "cancelat"

# Tabla de asociación para la relación ManyToMany entre Viatge 
# y Usuari (participants)
viatge_participants = Table(
    'viatge_participants',
    Base.metadata,
    Column('viatge_id', Integer, ForeignKey('viatges.id'), primary_key=True),
    Column('usuari_id', Integer, ForeignKey('usuaris.id'), primary_key=True)
)

class Viatge(Base):
    __tablename__ = "viatges"
    
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(200), nullable=False)
    desti = Column(String(200), nullable=False)
    data_inici = Column(Date, nullable=False)
    data_fi = Column(Date, nullable=False)
    descripcio = Column(Text, nullable=True)
    maxim_participants = Column(Integer, nullable=False)
    total_participants = Column(Integer, default=0, nullable=False)
    estat = Column(SQLEnum(EstatViatge), default=EstatViatge.PLANIFICANT, 
                   nullable=False)
    
    # ForeignKey: creador del viaje
    creador_id = Column(Integer, ForeignKey('usuaris.id'), nullable=False)
    
    # Relaciones

    creador = relationship("Usuari", foreign_keys=[creador_id], 
                           backref="viatges_creats")
    participants = relationship("Usuari", secondary=viatge_participants, 
                                backref="viatges_inscrits")
    
    