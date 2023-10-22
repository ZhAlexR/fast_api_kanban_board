from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.board import create, read_all
from backend.app.schemas import BoardCreate, Board
from backend.app.services.tags import Tags

router = APIRouter(prefix="/boards", tags=[Tags.BOARD])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(request: BoardCreate, db: Session = Depends(get_db)):
    return create(request, db)


@router.get("/list", status_code=status.HTTP_200_OK, response_model=list[Board])
def list_task(db: Session = Depends(get_db)):
    return read_all(db)
