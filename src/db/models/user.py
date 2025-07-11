from sqlalchemy import Column, Integer, String, Date, Boolean, TIMESTAMP, func
from src.db.session import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "kevyn_store"}


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    birthday = Column(Date)
    is_admin = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
