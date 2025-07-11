from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db.models.user import User
from src.db.models.wallet import Wallet
from src.schemas.user import UserChangePassword
from src.services.auth_service import AuthService, pwd_context
from src.schemas.user import UserSelfUpdate

    





class UserService:    
    def create_user(user_data, db: Session):
        existing_user = db.query(User).filter(User.username == user_data.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")
            
        hashed_pw = AuthService.get_password_hash(user_data.password)
        db_user = User(
            username=user_data.username,
            hashed_password=hashed_pw,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            age=user_data.age,
            birthday=user_data.birthday
        )
        db.add(db_user)
        db.flush()

        db_wallet = Wallet(
            user_id=db_user.id,
            balance=0.0  
        )
        db.add(db_wallet)  
        db.commit()
        db.refresh(db_user)
        return db_user

    def update_my_info(
        id: int,
        updated_info: UserSelfUpdate,
        db: Session
    ):
        user = db.query(User).filter(User.id == id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        for key, value in updated_info.dict(exclude_unset=True).items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)
        return user


    

    def change_password(
        id: int, 
        password_data: UserChangePassword,
        db: Session):
        user = db.query(User).filter(User.id == id).first()

        if not user:
            raise Exception("User not found")
        if not pwd_context.verify(password_data.old_password, user.hashed_password):
            raise Exception("incorrect old password")

        user.hashed_password = AuthService.get_password_hash(password_data.new_password)
        db.commit()
        db.refresh(user)
        return user












