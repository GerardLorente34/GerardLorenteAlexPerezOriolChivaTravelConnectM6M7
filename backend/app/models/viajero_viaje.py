

# from sqlalchemy import Column, Integer, ForeignKey, Date
# from sqlalchemy.orm import relationship
# from ..db.database import Base

# class VaijeroViaje(Base):
#     __tablename__ = "viajero_viaje"
#
#     viejero_id = Column(Integer, ForeignKey("viajero.id"), primary_key=True)
#     curso_id = Column(Integer, ForeignKey("viaje.id"), primary_key=True)
#     fecha_inscripcion = Column(Date, nullable=False)
#
#     viajero = relationship("Viajero", back_populates="viaje")
#     viaje = relationship("Viaje", back_populates="viajeros")