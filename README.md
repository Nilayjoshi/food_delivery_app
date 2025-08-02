🍽️ Food Delivery Microservices
      - This is a simple food delivery app built using FastAPI and SQLAlchemy, structured as three independent microservices.

🔧 Microservices Overview
1. User Service (localhost:8000)
      - Handles users, placing orders, and ratings.

2. Restaurant Service (localhost:8001)
      - Handles restaurants, menus, and order processing.

3. Delivery Agent Service (localhost:8002)
      - Handles delivery agents and updating delivery statuses.

🚀 How to Run
Run each microservice separately with different ports:

      - uvicorn user_services.main:app --port 8000
      - uvicorn restaurant_services.main:app --port 8001
      - uvicorn delivery_agent_services.main:app --port 8002
