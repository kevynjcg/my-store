from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.db.session import Base

class GcashCard(Base):
    __tablename__ = "card_list"
    __table_args__ = {"schema": "kevyn_store"}  # if you use schemas

    id = Column(Integer, primary_key=True, index=True)  
    card_number = Column(String(16))  
    expiration_date = Column(String(5))
    cvv = Column(String(4))
    brand = Column(String(20))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    first_name = Column(String) 
    last_name = Column(String)
    balance = Column(Numeric(10, 2), default=0.00)