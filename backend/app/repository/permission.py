from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import PermissionCreate


def create(request: PermissionCreate, db: Session):
    new_permission = models.Permission(name=request.name)
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return new_permission


def read_all(db: Session):
    return db.query(models.Permission).all()
