from enum import Enum


class Tags(Enum):
    TEAM = "Team"
    USER = "User"
    ROLE = "Role"
    PERMISSION = "Permission"


tags_metadata = [
    {
        "name": "User",
        "description": "Operations with users",
    },
    {
        "name": "Team",
        "description": "Operation with team",
    },
    {
        "name": "Role",
        "description": "Operation with role",
    },
    {
        "name": "Permission",
        "description": "Operation with permission",
    },
]
