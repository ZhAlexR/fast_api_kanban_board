from pydantic import BaseModel, constr, EmailStr
from typing import List, Optional


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
    role: Optional[Role] = None

    class Config:
        from_attributes = True
