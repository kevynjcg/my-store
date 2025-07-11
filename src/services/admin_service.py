from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.db.models.user import User
from src.schemas.auth import Token
from src.schemas.user import UserCreate, AdminUserUpdate
from src.services.auth_service import AuthService



class AdminService:
    @staticmethod
    def admin_get_users(db: Session):
        return db.query(User).order_by(User.id).all()

    def admin_user_update(
        id: int,
        update_field: AdminUserUpdate,
        db: Session
    ):
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        for key, value in update_field.dict(exclude_unset=True).items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        return user

    def admin_change_password(
        id: int, 
        new_password: str, 
        db: Session
        ):
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise Exception("User not found")
        user.hashed_password = AuthService.get_password_hash(new_password)
        db.commit()
        db.refresh(user)
        return user
