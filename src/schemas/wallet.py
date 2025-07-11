from pydantic import BaseModel
from decimal import Decimal
from datetime import date, datetime

class WalletRead(BaseModel):
    balance: Decimal

    class Config:
        orm_mode = True

class CashInRequest(BaseModel):
    amount: Decimal
    