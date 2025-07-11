from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.db.models.user import User
from src.schemas.auth import Token
from src.schemas.user import UserCreate



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class AuthService:
    def get_password_hash(password):
        return pwd_context.hash(password)

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)


    def authenticate_user(username: str, password: str, db: Session):
        user = db.query(User).filter(User.username == username).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
        if not AuthService.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
        return user


        
