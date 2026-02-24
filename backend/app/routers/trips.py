from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.deps import get_db
from ..crud.viaje import (
    get_viajes_disponibles,
    get_viaje,
    inscribir_viajero,
    desinscribir_viajero,
)
from ..schemas.viajero_viaje import ViajeResponse
from ..utils.auth import get_current_user_from_token
from ..models.usuario import Usuario

router = APIRouter(prefix="/trips", tags=["trips"])

@router.get("/", response_model=list[ViajeResponse])
def list_available_trips(
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viajes = get_viajes_disponibles(db)

    for viaje in viajes:
        viaje.estoy_inscrito = any(
            v.id == current_user.id for v in viaje.participantes
        )
        viaje.soy_creador = (viaje.creador_id == current_user.id)

    return viajes

@router.get("/{id}", response_model=ViajeResponse)
def get_trip_detail(
    id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viaje = get_viaje(db, id)
    if not viaje:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    viaje.estoy_inscrito = any(
        v.id == current_user.id for v in viaje.participantes
    )

    viaje.soy_creador = (viaje.creador_id == current_user.id)

    return viaje


@router.post("/{id}/enroll", response_model=ViajeResponse)
def enroll_in_trip(
    id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viaje, error = inscribir_viajero(db, id, current_user.id)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return viaje

@router.post("/{id}/leave", response_model=ViajeResponse)
def leave_trip(
    id: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token)
):
    viaje, error = desinscribir_viajero(db, id, current_user.id)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return viaje
