from backend.app.models import Board
from backend.app.repository.base_crud import CRUDBase
from backend.app.schemas.schemas import BoardUpdate, BoardCreate


class CRUDBoard(CRUDBase[Board, BoardCreate, BoardUpdate]):
    pass


board = CRUDBoard(Board)
