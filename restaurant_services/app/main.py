from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include API routes
app.include_router(router, prefix="/restaurants", tags=["Restaurant Services"])
