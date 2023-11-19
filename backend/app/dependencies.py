from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal
from backend.app.models import User
from backend.app.repository.user import user
from backend.app.services.security import decode_access_token

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/login/get-token"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(reusable_oauth2)
) -> User:
    token_data = decode_access_token(access_token=token)
    current_user = user.get_by_email(db, email=token_data)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user
