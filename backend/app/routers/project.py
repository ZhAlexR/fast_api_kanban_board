from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.project import project
from backend.app.schemas.schemas import ProjectCreate, ProjectBase
from backend.app.services.tags import Tags

router = APIRouter(prefix="/projects", tags=[Tags.PROJECT])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_project(request: ProjectCreate, db: Session = Depends(get_db)):
    return project.create(request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProjectBase])
def list_project(db: Session = Depends(get_db)):
    return project.get_all(db)
