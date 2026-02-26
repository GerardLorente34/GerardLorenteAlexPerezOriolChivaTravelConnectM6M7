from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..crud.viaje import create_viaje, delete_viaje, get_viaje, update_viaje
from ..db.deps import get_db
from ..models.usuario import RolUsuario, Usuario
from ..schemas.viajero_viaje import ViajeCreate, ViajeResponse, ViajeUpdate
from ..utils.auth import get_current_user_from_token


router = APIRouter(prefix="/creator", tags=["creator"])


def _require_creator_or_admin(current_user: Usuario) -> None:
	if current_user.rol not in (RolUsuario.CREADOR, RolUsuario.ADMINISTRADOR):
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado")


@router.post("/trips", response_model=ViajeResponse, status_code=status.HTTP_201_CREATED)
def create_trip(
    viaje: ViajeCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token),
):
    _require_creator_or_admin(current_user)

    nuevo_viaje = create_viaje(db, viaje, current_user.id)

    nuevo_viaje.estoy_inscrito = False
    nuevo_viaje.soy_creador = True

    return nuevo_viaje

@router.put("/trips/{id}", response_model=ViajeResponse)
def update_own_trip(
    id: int,
    viaje: ViajeUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user_from_token),
):
    _require_creator_or_admin(current_user)

    db_viaje = get_viaje(db, id)
    if not db_viaje:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")

    if db_viaje.creador_id != current_user.id and current_user.rol != RolUsuario.ADMINISTRADOR:
        raise HTTPException(status_code=403, detail="No puedes modificar este viaje")

    updated, error = update_viaje(db, id, viaje)
    if error:
        raise HTTPException(status_code=400, detail=error)

    updated.estoy_inscrito = any(
        v.id == current_user.id for v in updated.participantes
    )
    updated.soy_creador = (updated.creador_id == current_user.id)

    return updated


@router.delete("/trips/{id}")
def delete_own_trip(
	id: int,
	db: Session = Depends(get_db),
	current_user: Usuario = Depends(get_current_user_from_token),
):
	_require_creator_or_admin(current_user)

	db_viaje = get_viaje(db, id)
	if not db_viaje:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Viaje no encontrado")
	if db_viaje.creador_id != current_user.id and current_user.rol != RolUsuario.ADMINISTRADOR:
		raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No puedes eliminar este viaje")

	success, error = delete_viaje(db, id)
	if error or not success:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error or "No se pudo eliminar")
	return {"detail": "Viaje eliminado"}
