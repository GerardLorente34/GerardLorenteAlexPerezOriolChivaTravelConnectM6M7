from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.deps import get_db
# from ..crud.viajero import
# from ..schemas.viajero_viaje import

router = APIRouter(prefijo="/viajeros", tags=["viajeros"])

# Mostramos todos los viajeros
@router.get("/", response_model=list[ViajeroResponse])
def read_viajeros(db: Session = Depends(get_db)):
    return get_viajeros(db)

# Mostrar un viajero por su ID con sus viajes
@router.get("/{viajero_id}/viajes", response_model=ViajeroViajesResponse)
def read_viajero(viajero_id: int, db: Session = Depends(get_db)):
    db_viajero = get_viajero(db, viajero_id) 