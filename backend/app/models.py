from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.database import Base

metadata = Base.metadata

role_permission_association = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    permissions = relationship(
        "Permission", secondary=role_permission_association, back_populates="roles"
    )
    user_id = Column(Integer, ForeignKey("users.id"), default=None)
    user = relationship("User", back_populates="role")


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    roles = relationship(
        "Role", secondary=role_permission_association, back_populates="permissions"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = relationship("Role", uselist=False, back_populates="user")
