from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.board import board
from backend.app.schemas.schemas import BoardCreate, BoardBase
from backend.app.services.tags import Tags

router = APIRouter(prefix="/boards", tags=[Tags.BOARD])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_board(request: BoardCreate, db: Session = Depends(get_db)):
    return board.create(request, db)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[BoardBase])
def list_board(db: Session = Depends(get_db)):
    return board.get_all(db)
