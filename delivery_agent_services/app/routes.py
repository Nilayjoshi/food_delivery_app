from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("delivery_agent_services_logs")

router = APIRouter()
logger.info('Delivery Agent Services API instance is created')

# Route to create a new delivery agent
@router.post("/create_agent/", response_model=schemas.DeliveryAgentOut)
def create_agent(data: schemas.DeliveryAgentCreate, db: Session = Depends(get_db)):
    agent = models.DeliveryAgent(**data.model_dump())
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

# Route to update agent availability
@router.patch("/update_agent_availability/{agent_id}/", response_model=schemas.DeliveryAgentOut)
def update_agent_availability(agent_id: int, data: schemas.UpdateAgentAvailability, db: Session = Depends(get_db)):
    agent = db.query(models.DeliveryAgent).get(agent_id)
    agent.availability = data.availability
    db.commit()
    db.refresh(agent)
    return agent

# For update delivery status
@router.put("/update_delivery_status/{order_id}/", response_model=schemas.DeliveryStatusOut)
def update_delivery_status(order_id: int, data: schemas.UpdateDeliveryStatus, db: Session = Depends(get_db)):
    status = models.DeliveryStatus(order_id=order_id, status=data.status)
    db.add(status)
    db.commit()
    db.refresh(status)
    return status

# Route to get all available delivery agents
@router.get("/get_available_agents/", response_model=list[schemas.DeliveryAgentOut])
def get_available_agents(db: Session = Depends(get_db)):
    return db.query(models.DeliveryAgent).filter(models.DeliveryAgent.availability == True).all()
