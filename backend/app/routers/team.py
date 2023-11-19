from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.team import team
from backend.app.schemas.schemas import TeamCreate, TeamBase
from backend.app.services.tags import Tags

router = APIRouter(prefix="/teams", tags=[Tags.TEAM])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_team(request: TeamCreate, db: Session = Depends(get_db)):
    return team.create(db, income_entity=request)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TeamBase])
def list_task(db: Session = Depends(get_db)):
    return team.get_all(db)
