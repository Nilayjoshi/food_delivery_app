from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql import func

# User table stores basic user info
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    orders = relationship("Order", back_populates="user")
    ratings = relationship("Rating", back_populates="user")

# Order table stores which user ordered from which restaurant and when
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    restaurant_id = Column(Integer, nullable=False) 
    items = Column(JSON, nullable=False)  
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")
    rating = relationship("Rating", back_populates="order", uselist=False)

# Rating table lets users rate both order and delivery agent
class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    order_rating = Column(Float)     
    delivery_agent_rating = Column(Float)

    user = relationship("User", back_populates="ratings")
    order = relationship("Order", back_populates="rating")
