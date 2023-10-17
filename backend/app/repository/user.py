from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import UserCreate
from backend.app.services.security import hash_password


def create(request: UserCreate, db: Session):
    hashed_password = hash_password(request.password)

    user_data = request.model_dump()
    user_data["password"] = hashed_password

    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
