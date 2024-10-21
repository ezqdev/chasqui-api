from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    delivery_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    status = Column(Enum("pending", "in_progress", "delivered", name="order_status"))
    created_at = Column(DateTime)
    
    client = relationship("User", foreign_keys=[client_id])
    delivery = relationship("User", foreign_keys=[delivery_id])