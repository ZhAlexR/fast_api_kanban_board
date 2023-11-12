from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import user, permission, team, role, board, project, task, login
from backend.app.services.tags import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)

origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

app.include_router(router=user.router)
app.include_router(router=permission.router)
app.include_router(router=team.router)
app.include_router(router=role.router)
app.include_router(router=board.router)
app.include_router(router=project.router)
app.include_router(router=task.router)
app.include_router(router=login.router)
