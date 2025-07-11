from fastapi import APIRouter, Depends
from src.api.v1.endpoints.auth import auth
from src.api.v1.endpoints.user import users
from src.api.v1.endpoints.admin import admin
from src.api.v1.endpoints.wallet import wallet
from src.api.v1.endpoints.cards import cards
from src.core.security import get_admin_user, get_current_user

api_router = APIRouter()

api_router.include_router(
    auth, 
    prefix="/auth", 
    tags=["Auth"]
)


api_router.include_router(
    users, 
    prefix="/users", 
    tags=["Users"],
    dependencies=[Depends(get_current_user)]
)


api_router.include_router(
    admin, 
    prefix="/admin", 
    tags=["Admin"],
    dependencies=[Depends(get_admin_user)]
)

api_router.include_router(
    wallet, 
    prefix="/me/wallet", 
    tags=["Wallet"],
    dependencies=[Depends(get_current_user)]
)


api_router.include_router(
    cards, 
    prefix="/me/card", 
    tags=["Card"],
    dependencies=[Depends(get_current_user)]
)





