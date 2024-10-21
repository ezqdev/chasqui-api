from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    status: str

class OrderCreate(OrderBase):
    client_id: int

class OrderUpdate(OrderBase):
    delivery_id: Optional[int] = None

class OrderInDB(OrderBase):
    id: int
    client_id: int
    delivery_id: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

class Order(OrderInDB):
    pass