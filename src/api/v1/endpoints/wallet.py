from fastapi import APIRouter, Depends, HTTPException
from src.db.session import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from src.schemas.wallet import WalletRead, CashInRequest
from src.services.wallet_service import WalletService
from src.core.security import get_admin_user, get_current_user
from src.db.models.user import User



wallet = APIRouter()


@wallet.get("/balance", response_model=WalletRead)
def get_my_wallet(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return WalletService.get_wallet_for_user(user_id=current_user.id, db=db)

@wallet.post("/cash-in", response_model=WalletRead)
def cash_in(
    cash_amount: CashInRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return WalletService.cash_in_for_user(cash_amount, user_id=current_user.id, db=db) 