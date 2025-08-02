from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("restaurant_services_logs")

router = APIRouter()
logger.info('Restaurant Services API instance is created')

# Create a new restaurant
@router.post("/create_restaurant/", response_model=schemas.RestaurantOut)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = models.Restaurant(**restaurant.model_dump())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

# Add menu item to a restaurant
@router.post("/add_menu_item/{restaurant_id}", response_model=schemas.MenuItemOut)
def add_menu_item(restaurant_id: int, item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    menu = models.MenuItem(restaurant_id=restaurant_id, **item.model_dump())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

# Create restaurant order
@router.post("/create_restaurant_order/", response_model=schemas.RestaurantOrderOut)
def create_restaurant_order(order: schemas.RestaurantOrderCreate, db: Session = Depends(get_db)):
    db_order = models.RestaurantOrder(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Set restaurant online/offline
@router.put("/update_availability/{restaurant_id}/", response_model=schemas.RestaurantOut)
def update_availability(restaurant_id: int, data: schemas.RestaurantAvailabilityUpdate, db: Session = Depends(get_db)):
    restaurant = db.query(models.Restaurant).get(restaurant_id)
    restaurant.is_online = data.is_online
    db.commit()
    db.refresh(restaurant)
    return restaurant

# Receive order
@router.post("/receive_order/", response_model=schemas.RestaurantOrderOut)
def receive_order(order: schemas.RestaurantOrderCreate, db: Session = Depends(get_db)):
    db_order = models.RestaurantOrder(**order.model_dump(), status=schemas.OrderStatus.PENDING)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Process order
@router.put("/process_order/{order_id}/", response_model=schemas.RestaurantOrderOut)
def process_order(order_id: int, update: schemas.ProcessOrder, db: Session = Depends(get_db)):
    order = db.query(models.RestaurantOrder).filter(models.RestaurantOrder.id == order_id).first()
    if order:
        order.status = update.status
        db.commit()
        db.refresh(order)
    return order

# Get menu of a restaurant
@router.get("/get_restaurant_menu/{restaurant_id}/", response_model=list[schemas.MenuItemOut])
def get_restaurant_menu(restaurant_id: int, db: Session = Depends(get_db)):
    return db.query(models.MenuItem).filter(models.MenuItem.restaurant_id == restaurant_id).all()

# Get available restaurants
@router.get("/get_available_restaurants/", response_model=list[schemas.RestaurantOut])
def get_available_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Restaurant).filter(models.Restaurant.is_online == True).all()

# Delivery agent assignment function
def assign_delivery_agent() -> int:
    return 1 