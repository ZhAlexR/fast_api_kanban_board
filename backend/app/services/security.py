from datetime import timedelta, datetime
from typing import Union, Any

from passlib.context import CryptContext
from jose import jwt

from backend.configuration.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password):
    return pwd_context.verify(password, hashed_password)


def create_access_token(sub: Union[str, Any], expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    access_token_data = {"sub": sub, "exp": expire}
    return jwt.encode(access_token_data, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)