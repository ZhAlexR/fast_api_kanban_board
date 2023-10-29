from enum import Enum


class Tags(Enum):
    TEAM = "Team"
    USER = "User"
    ROLE = "Role"
    PERMISSION = "Permission"
    TASK = "Task"
    BOARD = "Board"
    PROJECT = "Project"


tags_metadata = [
    {
        "name": "Permission",
        "description": "Operation with permission",
    },
    {
        "name": "Role",
        "description": "Operation with role",
    },
    {
        "name": "User",
        "description": "Operations with users",
    },
    {
        "name": "Team",
        "description": "Operation with team",
    },
    {
        "name": "Board",
        "description": "Operation with board",
    },
    {
        "name": "Project",
        "description": "Operation with project",
    },
    {
        "name": "Task",
        "description": "Operation with task",
    },
]
