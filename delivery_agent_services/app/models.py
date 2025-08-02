from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from .database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# DeliveryAgent model to store basic delivery agent details and availability
class DeliveryAgent(Base):
    __tablename__ = "delivery_agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    availability = Column(Boolean, default=True) 

    deliveries = relationship("DeliveryStatus", back_populates="agent")

class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, nullable=False)
    agent_id = Column(Integer, ForeignKey("delivery_agents.id"))
    status = Column(String, default="assigned")
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    agent = relationship("DeliveryAgent", back_populates="deliveries")
