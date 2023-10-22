from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import ProjectCreate


def create(request: ProjectCreate, db: Session):
    new_project = models.Project(**request.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def get_by_id(id_: int, db: Session):
    return db.query(models.Project).filter(models.Project.id == id_).first()


def read_all(db: Session):
    return db.query(models.Project).all()
