from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    birthday: Optional[date] = None

class UserSelfRead(BaseModel):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    birthday: Optional[date]

    class Config:
        orm_mode = True

class UserSelfUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str]= None
    age: Optional[int]= None
    birthday: Optional[date]= None

class UserChangePassword(BaseModel):
    old_password: str
    new_password: str    
#admin

class AdminUserUpdate(BaseModel):
    username: Optional[str]= None
    first_name: Optional[str]= None
    last_name: Optional[str]= None
    age: Optional[int]= None
    birthday: Optional[date]= None
    is_admin: Optional[bool]= None

class AdminChangeUserPassword(BaseModel):
    new_password: str    


class AdminUsersInfo(BaseModel):
    id: int
    username: str
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    birthday: date | None = None
    is_admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class MessageResponse(BaseModel):
    message: str

class MessageResponseRegister(BaseModel):
    message: str
