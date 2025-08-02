🍽️ Food Delivery Microservices
This is a simple food delivery app built using FastAPI and SQLAlchemy, structured as three independent microservices.

🔧 Microservices Overview
1. User Service (localhost:8000)
Handles users, placing orders, and ratings.

Endpoints:
POST /create_user – Create a new user

GET /retrieve_online_restaurants/{hour} – List restaurants online at a given hour

GET /get_restaurant_menu/{restaurant_id} – View specific restaurant's menu

POST /place_order – Place a food order

POST /leave_rating/{order_id} – Leave a rating for the order and delivery agent

2. Restaurant Service (localhost:8001)
Handles restaurants, menus, and order processing.

Endpoints:
POST /create_restaurant – Create a new restaurant

PUT /update_menu/{restaurant_id} – Update menu items and prices

PUT /update_availability/{restaurant_id} – Update online/offline status

POST /receive_order – Receive an order from User Service

3. Delivery Agent Service (localhost:8002)
Handles delivery agents and updating delivery statuses.

Endpoints:
POST /create_agent – Register a new delivery agent

PUT /update_availability/{agent_id} – Set delivery agent availability

PUT /update_delivery_status/{order_id} – Update the delivery status

🚀 How to Run
Run each microservice separately with different ports:

uvicorn user_services.main:app --port 8000
uvicorn restaurant_services.main:app --port 8001
uvicorn delivery_agent_services.main:app --port 8002
