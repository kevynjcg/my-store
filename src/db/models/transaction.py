from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.db.session import Base

class Transaction(Base):
    __tablename__ = "transactions"
    __table_args__ = {"schema": "kevyn_store"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    card_id = Column(Integer, ForeignKey("cards.id", ondelete="SET NULL"))
    material_id = Column(Integer, ForeignKey("materials.id", ondelete="SET NULL"))
    amount = Column(Numeric(10, 2), nullable=False)
    type = Column(String(50), nullable=False)  # e.g., 'cash_in', 'purchase'
    description = Column(String(255))
    status = Column(String(50), default="completed")
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    user = relationship("User", backref="transactions")
    card = relationship("Card", backref="transactions")
    material = relationship("Material", backref="transactions")
