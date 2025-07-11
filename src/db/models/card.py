from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.db.session import Base

class Card(Base):
    __tablename__ = "cards"
    __table_args__ = {"schema": "kevyn_store"}

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String(16))  
    expiration_date = Column(String(5))
    cvv = Column(String(4))
    brand = Column(String(20))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    first_name = Column(String) 
    last_name = Column(String) 
    user_id = Column(Integer, ForeignKey("kevyn_store.users.id", ondelete="CASCADE"), unique=True)

    user = relationship("User", backref="card")
