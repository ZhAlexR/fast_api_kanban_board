from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from beckend.app import models
from beckend.app.database import engine

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins)

models.Base.metadata.create_all(bind=engine)
