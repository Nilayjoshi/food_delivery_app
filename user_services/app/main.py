from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

# Auto-create tables if they don’t exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="User Services - Food Delivery App"
)

# Include router
app.include_router(router,  prefix="/users", tags=["Users"])
