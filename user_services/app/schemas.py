from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    PROCESSING = "processing"
    COMPLETED = "completed"

# User schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr

class OrderItem(BaseModel):
    item: str
    qty: int

# Order schemas
class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    items: list[OrderItem]

class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    restaurant_id: int
    items: list[OrderItem]
    created_at: datetime

# Rating schemas
class RatingCreate(BaseModel):
    user_id: int
    order_rating: Optional[float]
    delivery_agent_rating: Optional[float]

class RatingOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    order_id: int
    order_rating: Optional[float]
    delivery_agent_rating: Optional[float]
