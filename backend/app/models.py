from enum import Enum as PyEnum
from datetime import datetime

from sqlalchemy import Column, String, Integer, Table, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship

from backend.app.database import Base

metadata = Base.metadata


class TaskPriority(PyEnum):
    URGENT = "Urgent"
    MAJOR = "Major"
    MINOR = "Minor"


role_permission_association = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)

board_team_association = Table(
    "board_team",
    Base.metadata,
    Column("board_id", Integer, ForeignKey("boards.id")),
    Column("team_id", Integer, ForeignKey("teams.id")),
)

board_project_association = Table(
    "board_project",
    Base.metadata,
    Column("board_id", Integer, ForeignKey("boards.id")),
    Column("project_id", Integer, ForeignKey("projects.id")),
)

team_project_association = Table(
    "team_project",
    Base.metadata,
    Column("team_id", Integer, ForeignKey("teams.id")),
    Column("project_id", Integer, ForeignKey("projects.id")),
)


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), default=None)
    user = relationship("User", back_populates="role")

    permissions = relationship(
        "Permission", secondary=role_permission_association, back_populates="roles"
    )


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    roles = relationship(
        "Role", secondary=role_permission_association, back_populates="permissions"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=63))
    surname = Column(String(length=63))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), default=None)

    team = relationship("Team", back_populates="members")
    role = relationship("Role", uselist=False, back_populates="user")
    owned_tasks = relationship(
        "Task", back_populates="owner", foreign_keys="Task.owner_id"
    )
    assigned_tasks = relationship(
        "Task", back_populates="assigned", foreign_keys="Task.assigned_id"
    )


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(
        String(length=63),
    )
    description = Column(String)

    members = relationship("User", back_populates="team")
    boards = relationship(
        "Board", secondary=board_team_association, back_populates="teams"
    )
    projects = relationship(
        "Project", secondary=team_project_association, back_populates="teams"
    )


class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True)
    description = Column(String(length=255))

    teams = relationship(
        "Team", secondary=board_team_association, back_populates="boards"
    )
    projects = relationship(
        "Project", secondary=board_project_association, back_populates="boards"
    )


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=63))
    description = Column(String(length=255))

    boards = relationship(
        "Board", secondary=board_project_association, back_populates="projects"
    )
    teams = relationship(
        "Team", secondary=team_project_association, back_populates="projects"
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=63))
    description = Column(String(length=255))
    created_at = Column(DateTime, default=datetime.utcnow)
    expired_at = Column(DateTime)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MINOR, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))
    assigned_id = Column(Integer, ForeignKey("users.id"), default=None)
    owner = relationship("User", back_populates="owned_tasks", foreign_keys=[owner_id])
    assigned = relationship(
        "User", back_populates="assigned_tasks", foreign_keys=[assigned_id]
    )
