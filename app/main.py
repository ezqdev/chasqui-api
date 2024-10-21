from fastapi import FastAPI
from app.api import auth, users, orders
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(auth.router, tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}