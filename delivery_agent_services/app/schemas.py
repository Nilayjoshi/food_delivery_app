from datetime import datetime
from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional

class DeliveryStatus(str, Enum):
    PICKED_UP = "picked_up"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class DeliveryAgentBase(BaseModel):
    name: str
    availability: Optional[bool] = True
    
class DeliveryAgentCreate(DeliveryAgentBase):
    pass

class DeliveryAgentOut(DeliveryAgentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

class UpdateAgentAvailability(BaseModel):
    availability: bool

class UpdateDeliveryStatus(BaseModel):
    status: DeliveryStatus
    agent_id: Optional[int] = None

class DeliveryStatusOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    agent_id: Optional[int] = None
    status: DeliveryStatus
    updated_at: datetime
