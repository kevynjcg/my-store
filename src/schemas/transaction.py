from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: Decimal
    type: str   # 'cash_in', 'purchase', etc.
    description: Optional[str] = None
    card_id: Optional[int] = None
    material_id: Optional[int] = None

class TransactionRead(BaseModel):
    id: int
    user_id: int
    amount: Decimal
    type: str
    description: Optional[str]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
