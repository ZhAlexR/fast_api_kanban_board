from sqlalchemy.orm import Session

from backend.app import models
from backend.app.schemas import BoardCreate


def create(request: BoardCreate, db: Session):
    new_board = models.Board(**request.model_dump())
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    return new_board


def get_by_id(id_: int, db: Session):
    return db.query(models.Board).filter(models.Board.id == id_).first()


def read_all(db: Session):
    return db.query(models.Board).all()
