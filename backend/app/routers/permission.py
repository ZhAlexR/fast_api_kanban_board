from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.permission import create, read_all
from backend.app.schemas import PermissionCreate, PermissionList
from backend.app.services.tags import Tags

router = APIRouter(prefix="/permissions", tags=[Tags.PERMISSION])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_permission(request: PermissionCreate, db: Session = Depends(get_db)):
    return create(request, db)


@router.get("/list", response_model=list[PermissionList])
def list_permission(db: Session = Depends(get_db)):
    return read_all(db)
