from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime
from enum import Enum

# Enum for Order status
class OrderStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    PROCESSING = "processing"
    COMPLETED = "completed"

class MenuItemBase(BaseModel):
    name: str
    price: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemOut(MenuItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    restaurant_id: int

class RestaurantBase(BaseModel):
    name: str
    is_online: Optional[bool] = True

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantOut(RestaurantBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

class RestaurantAvailabilityUpdate(BaseModel):
    is_online: bool

class OrderItem(BaseModel):
    item: str
    qty: int

class RestaurantOrderCreate(BaseModel):
    user_id: int 
    restaurant_id: int
    items: List[OrderItem]
    created_at: datetime

class RestaurantOrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    restaurant_id: int
    user_id: int
    items: List[OrderItem]
    status: OrderStatus
    created_at: datetime
    delivery_agent_id: Optional[int] = None

class ProcessOrder(BaseModel):
    status: OrderStatus
