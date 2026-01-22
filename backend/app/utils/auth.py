from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from ..db.database import SessionLocal
from ..models.usuario import Usuario
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def _get_user_from_username(username: str) -> Optional[Usuario]:
    db = SessionLocal()
    try:
        return db.query(Usuario).filter(Usuario.username == username).first()
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme)) -> Usuario:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = _get_user_from_username(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    return user


def get_current_user_from_token(token: str = Depends(oauth2_scheme)) -> Usuario:
    # FastAPI usarà aquesta funció com a dependency a les rutes
    return get_current_user(token)


def authenticate_user(username: str, password: str) -> Optional[Usuario]:
    usuario = _get_user_from_username(username)
    if not usuario:
        return None
    if not verify_password(password, usuario.hashed_password):
        return None
    return usuario


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)