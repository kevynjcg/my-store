from fastapi import APIRouter, Depends, HTTPException
from src.db.session import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from src.schemas.user import UserSelfRead, AdminUsersInfo, AdminUserUpdate, AdminChangeUserPassword
from src.services.user_service import UserService
from src.services.admin_service import AdminService
from src.core.security import get_admin_user, get_current_user
from src.db.models.user import User


admin = APIRouter()




@admin.get("/users", response_model=list[AdminUsersInfo])
def admin_get_users(db: Session = Depends(get_db)):
    return  AdminService.admin_get_users(db)


@admin.patch("/users/{id}", response_model=AdminUsersInfo)
def admin_user_update(
    id: int,
    update_field: AdminUserUpdate,
    db: Session = Depends(get_db)
):
    return AdminService.admin_user_update(id, update_field, db)


@admin.patch("/users/{id}/password", response_model=AdminUsersInfo)
def admin_change_password(
    id: int,
    password_data: AdminChangeUserPassword,
    db: Session = Depends(get_db),
):
    try:
        user = AdminService.admin_change_password(id, password_data.new_password, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user    
