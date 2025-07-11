from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.config import settings
from src.db.session import get_db, SessionLocal, engine
from src.db.models.user import User
from src.schemas.auth import Token
from src.schemas.user import UserCreate, UserSelfRead
from src.services.auth_service import AuthService
from src.services.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import jwt


auth = APIRouter()


@auth.get("/")
def read_test():
    return {"message": "hello"}

@auth.post("/register", response_model=UserSelfRead)    
def register(
    user: UserCreate, 
    db: Session = Depends(get_db)
):

    return UserService.create_user(user, db)

@auth.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthService.authenticate_user(form_data.username, form_data.password, db)

    access_token_expires = timedelta(minutes=30)
    access_token = jwt.encode(
        {
            "sub": user.username,
            "exp": datetime.utcnow() + access_token_expires
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return {"access_token": access_token, "token_type": "bearer"}