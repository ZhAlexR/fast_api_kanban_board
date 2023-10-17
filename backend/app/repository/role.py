from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.app import models
from backend.app.schemas import RoleCreate


def create(request: RoleCreate, db: Session):
    permissions = (
        db.query(models.Permission)
        .filter(models.Permission.id.in_(request.permissions))
        .all()
    )

    # Check if all permission IDs are valid
    if len(permissions) != len(request.permissions):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid permission IDs"
        )

    new_role = models.Role(name=request.name, permissions=permissions)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def read_all(db: Session):
    return db.query(models.Role).all()
