from datetime import datetime, timedelta, date

from pydantic import BaseModel, constr, EmailStr, field_validator
from typing import List, Optional

from backend.app.models import TaskPriority


class PermissionBase(BaseModel):
    name: constr(min_length=1, max_length=255)


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(PermissionBase):
    pass


class PermissionList(PermissionBase):
    id: int

    class Config:
        from_attributes = True


class RoleBase(BaseModel):
    name: constr(min_length=1, max_length=255)


class RoleCreate(RoleBase):
    permissions: List[int] = []


class RoleUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = None
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


class UserUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=255)] = None
    surname: Optional[constr(min_length=1, max_length=255)] = None
    password: Optional[constr(min_length=1)] = None


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
    name: Optional[str] = None
    description: Optional[str] = None


class TeamCreate(TeamBase):
    members: list[int] = []
    boards: list[int] = []
    projects: list[int] = []


class TeamUpdate(TeamBase):
    members: Optional[list[int]] = None
    boards: Optional[list[int]] = None
    projects: Optional[list[int]] = None


class BoardBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class BoardCreate(BoardBase):
    teams: list[int] = []
    projects: list[int] = []


class BoardUpdate(BoardBase):
    teams: Optional[list[int]] = None
    projects: Optional[list[int]] = None


class BoardList(BaseModel):
    id: int
    name: str


class ProjectBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    boards: list[int] = []
    teams: list[int] = []


class ProjectUpdate(ProjectBase):
    boards: Optional[list[int]] = None
    teams: Optional[list[int]] = None


class TaskBase(BaseModel):
    name: str
    description: str


class TaskCreate(TaskBase):
    expired_at: str
    priority: TaskPriority = TaskPriority.MINOR
    assigned_id: Optional[int]

    @classmethod
    @field_validator(__field="expired_at", mode="before")
    def expired_at_validate(cls, value):
        if not value:
            return datetime.combine(
                date.today() + timedelta(days=1), datetime.min.time()
            )
        return value


class TaskUpdate(BaseModel):
    expired_at: Optional[str] = None
    priority: Optional[TaskPriority] = None
    assigned_id: Optional[int] = None
