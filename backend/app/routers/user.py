from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from backend.app import models
from backend.app.dependencies import get_db, get_current_user
from backend.app.repository.user import user
from backend.app.schemas.schemas import UserBase, UserCreate, UserList, UserUpdate, User
from backend.app.services.tags import Tags

router = APIRouter(prefix="/users", tags=[Tags.USER])


@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=UserBase)
async def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.put(path="/", status_code=status.HTTP_200_OK)
def update_user(request: UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return user.update(db, database_entity=current_user, income_entity=request)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[UserList])
def list_user(db: Session = Depends(get_db)):
    return user.get_all(db)
