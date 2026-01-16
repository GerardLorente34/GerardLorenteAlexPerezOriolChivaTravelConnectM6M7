from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.deps import get_db
from ..crud.viajero import (
    get_viajeros,
    get_viajero,
    create_viajero,
    delete_viajero,
    update_viajero,
)
from ..schemas.viajero_viaje import ViajeroCreate, ViajeroResponse, ViajeroUpdate

router = APIRouter(prefix="/viajeros", tags=["viajeros"])

@router.get("/", response_model=list[ViajeroResponse])
def read_viajeros(db: Session = Depends(get_db)):
    return get_viajeros(db)

@router.get("/{viajero_id}", response_model=ViajeroResponse)
def read_viajero(viajero_id: int, db: Session = Depends(get_db)):
    db_viajero = get_viajero(db, viajero_id)
    if not db_viajero:
        raise HTTPException(status_code=404, detail="Viajero not found")
    return db_viajero

@router.post("/", response_model=ViajeroResponse)
def create_viajero_endpoint(viajero: ViajeroCreate, db: Session = Depends(get_db)):
    return create_viajero(db, viajero)

@router.put("/{viajero_id}", response_model=ViajeroResponse)
def update_viajero_endpoint(viajero_id: int, viajero: ViajeroUpdate, db: Session = Depends(get_db)):
    db_viajero = update_viajero(db, viajero_id, viajero)
    if not db_viajero:
        raise HTTPException(status_code=404, detail="Viajero not found")
    return db_viajero

@router.delete("/{viajero_id}", response_model=dict)
def delete_viajero_endpoint(viajero_id: int, db: Session = Depends(get_db)):
    success = delete_viajero(db, viajero_id)
    if not success:
        raise HTTPException(status_code=404, detail="Viajero not found")
    return {"detail": "Viajero deleted"}
