from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import TaskCreate


def create(request: TaskCreate, db: Session):
    new_task = models.Task(**request.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_by_id(id_: int, db: Session):
    return db.query(models.Task).filter(models.Task.id == id_).first()


def read_all(db: Session):
    return db.query(models.Task).all()
