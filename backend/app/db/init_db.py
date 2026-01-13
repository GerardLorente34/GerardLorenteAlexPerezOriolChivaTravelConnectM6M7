from .database import Base, engine
# Importar todos los modelos para que SQLAlchemy los registre
from ..models import usuario, viajero, mensajesXat, peticionPromocion

Base.metadata.create_all(bind=engine)
