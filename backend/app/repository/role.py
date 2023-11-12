from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.app import models
from backend.app.models import Role
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import RoleCreate, RoleUpdate


class CRUDRole(CRUDBase[Role, RoleCreate, RoleUpdate]):
    def create(self, db: Session, *, income_entity: RoleCreate) -> Role:
        permissions = (
            db.query(models.Permission)
            .filter(models.Permission.id.in_(income_entity.permissions))
            .all()
        )

        # Check if all permission IDs are valid
        if len(permissions) != len(income_entity.permissions):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid permission IDs"
            )

        new_role = models.Role(name=income_entity.name, permissions=permissions)
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return new_role


role = CRUDRole(Role)
