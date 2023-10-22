from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import TeamCreate


def create(request: TeamCreate, db: Session):
    new_team = models.Team(**request.model_dump())
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


def get_by_id(id_: int, db: Session):
    return db.query(models.Team).filter(models.Team.id == id_).first()


def read_all(db: Session):
    return db.query(models.Team).all()
