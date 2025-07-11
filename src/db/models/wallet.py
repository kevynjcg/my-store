from sqlalchemy import Column, Integer, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.db.session import Base

class Wallet(Base):
    __tablename__ = "wallets"

    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True)
    balance = Column(Numeric(10, 2), default=0.00)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", backref="wallet")
