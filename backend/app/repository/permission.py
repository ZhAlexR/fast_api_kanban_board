from sqlalchemy.orm import Session

from backend.app.models import Permission
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import PermissionCreate, PermissionUpdate


class CRUDPermission(CRUDBase[Permission, PermissionCreate, PermissionUpdate]):
    pass


permission = CRUDPermission(Permission)
