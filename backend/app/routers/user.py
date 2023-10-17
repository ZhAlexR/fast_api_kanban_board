from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.user import create
from backend.app.schemas import UserBase, UserCreate
from backend.app.services.tags import Tags

router = APIRouter(prefix="/users", tags=[Tags.USER])


@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=UserBase)
async def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return create(request, db)
