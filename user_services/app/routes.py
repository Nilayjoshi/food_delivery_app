from fastapi import APIRouter, Depends, HTTPException
import httpx
from sqlalchemy.orm import Session
from . import schemas, models
from .database import get_db
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("user_services_logs")

router = APIRouter()
logger.info('User Services API instance is created')

# Create User
@router.post("/create_user/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get available restaurant
@router.get("/get_available_restaurants/")
def get_available_restaurants():
    response = httpx.get(f"http://localhost:8001/restaurants/get_available_restaurants/")
    return response.json()

# Place order
@router.post("/place_order/", response_model=schemas.OrderOut)
def place_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    # Sync order to restaurant service
    try:
        response = httpx.post(
            "http://localhost:8001/restaurants/receive_order",
            json={
                "order_id": db_order.id,
                "user_id": db_order.user_id,
                "restaurant_id": db_order.restaurant_id,
                "items": db_order.items,
                "created_at": db_order.created_at.isoformat()  
            }
        )
        response.raise_for_status()
    except httpx.RequestError as e:
        print(f"Request error: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.text}")

    return db_order

# Add rating endpoint
@router.post("/add_rating/{order_id}/", response_model=schemas.RatingOut)
def add_rating(order_id: int, rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    db_rating = models.Rating(order_id=order_id, **rating.model_dump())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

# get restaurant menu
@router.get("/get_restaurant_menu/{restaurant_id}/")
def get_restaurant_menu(restaurant_id: int):
    try:
        response = httpx.get(f"http://localhost:8001/restaurants/get_restaurant_menu/{restaurant_id}/")
        return response.json()
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch menu: {e}")
