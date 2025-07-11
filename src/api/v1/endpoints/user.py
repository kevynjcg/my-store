from fastapi import APIRouter, Depends, HTTPException
from src.db.session import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from src.schemas.user import UserSelfRead, UserSelfUpdate, UserChangePassword, MessageResponse
from src.services.user_service import UserService
from src.core.security import get_admin_user, get_current_user
from src.db.models.user import User

users = APIRouter()



@users.get("/me", response_model=UserSelfRead)
def get_my_info(current_user: User = Depends(get_current_user)):
    return current_user


@users.patch("/me", response_model=UserSelfRead)
def update_my_info(
    updated_info: UserSelfUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.update_my_info(current_user.id, updated_info, db)



@users.patch("/me/password", response_model=MessageResponse)
def change__my_password(
    password_data: UserChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user = UserService.change_password(current_user.id, password_data, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Password updated successfully"}   
