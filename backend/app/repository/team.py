from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import TeamCreate


def create(request: TeamCreate, db: Session):
    new_team = models.Team(**request.model_dump())
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team
