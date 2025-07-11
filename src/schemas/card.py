from pydantic import BaseModel
from datetime import datetime

from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class CardCreate(BaseModel):
    first_name: str
    last_name: str
    brand: str
    card_number: str
    expiration_date: str
    cvv: str

    class Config:
        orm_mode = True


class CardRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    brand: str
    card_number: str
    expiration_date: str
    cvv: str
    created_at: datetime

    class Config:
        orm_mode = True

class CardSafeRead(BaseModel):
    first_name: str
    last_name: str
    brand: str
    card_number: str      
    expiration_date: str

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, card):
        last4 = card.card_number[-4:] if card.card_number else ""
        masked = f"**** **** **** {last4}"
        return cls(
            first_name=card.first_name,
            last_name=card.last_name,
            brand=card.brand,
            card_number=masked,         
            expiration_date=card.expiration_date
        )


class CardUpdate(BaseModel):
    first_name: str
    last_name: str
    brand: str
    card_number: str
    expiration_date: str
    cvv: str

