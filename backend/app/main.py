from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette import status

from backend.app import models
from backend.app.database import engine
from backend.app.dependencies import get_db
from backend.app.schemas import RoleCreate, PermissionCreate, PermissionList, Role

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

models.Base.metadata.create_all(bind=engine)


@app.post("/role/", status_code=status.HTTP_201_CREATED)
def create_role(request: RoleCreate, db: Session = Depends(get_db)):
    permissions = (
        db.query(models.Permission)
        .filter(models.Permission.id.in_(request.permissions))
        .all()
    )

    # Check if all permission IDs are valid
    if len(permissions) != len(request.permissions):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid permission IDs"
        )

    new_role = models.Role(name=request.name, permissions=permissions)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


@app.get("/roles/", response_model=list[Role])
def list_roles(db: Session = Depends(get_db)):
    roles = db.query(models.Role).all()
    return roles


@app.post("/permission/", status_code=status.HTTP_201_CREATED)
def create_permission(request: PermissionCreate, db: Session = Depends(get_db)):
    new_permission = models.Permission(name=request.name)
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return new_permission


@app.get("/permissions/", response_model=list[PermissionList])
def list_permission(db: Session = Depends(get_db)):
    permission_list = db.query(models.Permission).all()
    return permission_list
