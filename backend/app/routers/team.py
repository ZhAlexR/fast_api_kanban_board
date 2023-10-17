from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.team import create
from backend.app.schemas import TeamCreate
from backend.app.services.tags import Tags

router = APIRouter(prefix="/teams", tags=[Tags.TEAM])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_team(request: TeamCreate, db: Session = Depends(get_db)):
    return create(request, db)
