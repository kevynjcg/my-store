from pydantic import BaseModel
from decimal import Decimal

class MaterialCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    in_stock: bool = True

class MaterialRead(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    in_stock: bool

    class Config:
        orm_mode = True

class MaterialUpdate(BaseModel):
    name: str
    description: str
    price: Decimal
    in_stock: bool
