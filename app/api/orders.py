from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, Order, OrderUpdate
from app.services import order_service
from app.db.session import get_db
from app.core.security import get_current_active_user
from app.schemas.user import User

router = APIRouter()

@router.post("/orders/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role != "client":
        raise HTTPException(status_code=403, detail="Only clients can create orders")
    return order_service.create_order(db=db, order=order)

@router.get("/orders/", response_model=list[Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role not in ["admin", "delivery"]:
        raise HTTPException(status_code=403, detail="Not authorized to view all orders")
    return order_service.get_orders(db, skip=skip, limit=limit)

@router.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update orders")
    return order_service.update_order(db=db, order_id=order_id, order=order)