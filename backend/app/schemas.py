from datetime import datetime, timedelta, date

from pydantic import BaseModel, constr, EmailStr, validator, field_validator
from typing import List, Optional

from backend.app.models import TaskPriority


class PermissionBase(BaseModel):
    name: constr(min_length=1, max_length=255)


class PermissionCreate(PermissionBase):
    pass


class PermissionList(PermissionBase):
    id: int

    class Config:
        from_attributes = True


class RoleBase(BaseModel):
    name: constr(min_length=1, max_length=255)


class RoleCreate(RoleBase):
    permissions: List[int] = []


class Role(RoleBase):
    id: int
    permissions: List[PermissionList] = []

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: constr(min_length=1, max_length=255)
    surname: constr(min_length=1, max_length=255)
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=1)


class User(UserBase):
    id: int
    role: Role = None

    class Config:
        from_attributes = True


class UserList(BaseModel):
    name: constr(min_length=1, max_length=255)
    email: EmailStr
    role: Optional[Role]


class TeamBase(BaseModel):
    name: str
    description: str


class TeamCreate(TeamBase):
    members: list[int] = []
    boards: list[int] = []
    projects: list[int] = []


class Board(BaseModel):
    name: str
    description: str


class BoardCreate(Board):
    teams: list[int] = []
    projects: list[int] = []


class BoardList(BaseModel):
    id: int
    name: str


class ProjectBase(BaseModel):
    name: str
    description: str


class ProjectCreate(ProjectBase):
    boards: list[int] = []
    teams: list[int] = []


class TaskBase(BaseModel):
    name: str
    description: str


class TaskCreate(TaskBase):
    expired_at: str
    priority: TaskPriority = TaskPriority.MINOR
    assigned_id: Optional[int]

    @field_validator(__field="expired_at", mode="before")
    @classmethod
    def expired_at_validate(cls, value):
        if not value:
            return datetime.combine(
                date.today() + timedelta(days=1), datetime.min.time()
            )
        return value
