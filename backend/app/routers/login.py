from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from backend.app.dependencies import get_db
from backend.app.repository.user import user
from backend.app.schemas.token import Token
from backend.app.services import security
from backend.app.services.tags import Tags
from backend.configuration.config import settings

router = APIRouter(prefix="/login", tags=[Tags.LOGIN])


@router.post("/get-token", status_code=status.HTTP_200_OK, response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    authenticated_user = user.authenticate(db, email=request.username, password=request.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {
        "access_token": security.create_access_token(
            authenticated_user.email, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
