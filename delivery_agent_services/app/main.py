from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router as delivery_agent_router

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include delivery agent routes
app.include_router(delivery_agent_router, prefix="/delivery-agents", tags=["Delivery Agents"])
