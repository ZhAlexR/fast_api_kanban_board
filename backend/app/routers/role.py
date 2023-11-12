from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.role import role
from backend.app.schemas.schemas import RoleCreate, Role
from backend.app.services.tags import Tags

router = APIRouter(prefix="/roles", tags=[Tags.ROLE])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_role(request: RoleCreate, db: Session = Depends(get_db)):
    return role.create(request, db)


@router.get("/", response_model=list[Role])
def list_roles(db: Session = Depends(get_db)):
    return role.get_all(db)


@router.delete("/{id}")
def delete_role(id_: int, db: Session = Depends(get_db)):
    return role.remove(db, id_=id_)
