from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date


# INPUT
class ViajeroCreate(BaseModel):
    username: str
    email: EmailStr
    nombre_completo: str
    bio: Optional[str] = None

class ViajeroUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    bio: Optional[str] = None

class ViajeCreate(BaseModel):
    nombre: str
    destino: str
    fecha_inicio: date
    fecha_fin: date
    descripcion: Optional[str] = None
    maximo_participantes: int

class ViajeUpdate(BaseModel):
    nombre: Optional[str] = None
    destino: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    descripcion: Optional[str] = None
    maximo_participantes: Optional[int] = None

# OUTPUT
class ViajeroResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    nombre_completo: str
    bio: Optional[str] = None

    class Config:
        from_attributes = True

class ViajeResponse(BaseModel):
    id: int
    nombre: str
    destino: str
    fecha_inicio: date
    fecha_fin: date
    descripcion: Optional[str] = None
    maximo_participantes: int
    total_participantes: int
    estado: str
    creador_id: int
    
    estoy_inscrito: bool = False
    soy_creador: bool

    class Config:
        from_attributes = True

# OUPUT ANIDADO

# Inscripcion al viaje
class InscripcionViaje(BaseModel):
    fecha_inscripcion: date
    viaje: ViajeResponse # nos unimos al viaje

    class Config:
        from_attributes = True

# Inscripcion del viajero
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