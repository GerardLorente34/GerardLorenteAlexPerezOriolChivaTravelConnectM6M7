from sqlalchemy import Column, Integer, String, Enum as SQLEnum, Text
from ..db.database import Base
import enum

# Enum para el estado de la promoción
class EstatPromocio(str, enum.Enum):
    Pendent = "pendent"
    Aprovat = "aprovat"
    Rebutjada = "rebutjada"
    