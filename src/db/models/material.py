from sqlalchemy import Column, Integer, String, Numeric, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from src.db.session import Base

class Material(Base):
    __tablename__ = "materials"
    __table_args__ = {"schema": "kevyn_store"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
