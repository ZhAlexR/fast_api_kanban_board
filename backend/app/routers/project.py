from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.project import create, read_all
from backend.app.schemas import ProjectCreate, ProjectBase
from backend.app.services.tags import Tags

router = APIRouter(prefix="/projects", tags=[Tags.PROJECT])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(request: ProjectCreate, db: Session = Depends(get_db)):
    return create(request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProjectBase])
def list_task(db: Session = Depends(get_db)):
    return read_all(db)
