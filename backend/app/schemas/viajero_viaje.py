from pydantic import BaseModel
from typing import List, Optional
from datetime import date


#INPUT
class ViajeroCreate(BaseModel):
    nombre: str
    email: str

class ViajeroUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None

class ViajeCreate(BaseModel):
    nombre: str

class ViajeUpdate(BaseModel):
    nombre: Optional[str] = None

#OUTPUT

class ViajeroResponse(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        from_attributes = True

class ViajeResponse(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True

# OUPUT ANIDADO

#Inscripcion al viaje
class InscripcionViaje(BaseModel):
    fecha_inscripcion: date
    viaje: ViajeResponse # nos unimos al viaje

    class Config:
        from_attributes = True

#Inscripcion del viajero
class InscripcionViajero(BaseModel):
    fecha_inscripcion: date
    viajero: ViajeroResponse #unimos al viajero

    class Config:
        from_attributes = True

class ViajeroViajeResponse(ViajeroResponse):
    viajes: List[InscripcionViaje] = []

    class Config:
        from_attributes = True

class ViajeViajeroResponse(ViajeResponse):
    viajeros: List[InscripcionViajero] = []

    class Config:
        from_attributes = True

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class CambiarViajeRequest(BaseModel):
    viajero_id: int
    viaje_inicial_id: int
    viaje_final_id: int