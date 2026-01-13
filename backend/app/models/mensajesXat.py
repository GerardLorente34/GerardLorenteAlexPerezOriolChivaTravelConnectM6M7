from sqlalchemy import Column, Integer, Enum as SQLEnum, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base


class MissatgeXat(Base):
    __tablename__ = "mensajes"
    
    id = Column(Integer, primary_key=True, index=True)