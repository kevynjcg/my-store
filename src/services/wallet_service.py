from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db.models.wallet import Wallet
from src.db.models.card import Card
from src.schemas.wallet import WalletRead, CashInRequest
from src.db.models.card_list import GcashCard



    
class WalletService:
    @staticmethod
    def get_wallet_for_user(user_id: int, db: Session):
        wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
        if not wallet:
            raise HTTPException(status_code=404, detail="Wallet not found")
        return wallet

 

    def cash_in_for_user(cash_amount: CashInRequest, user_id= int, db = Session)  :
        card = db.query(Card).filter(Card.user_id == user_id).first()
        if not card:
            raise HTTPException(status_code=404, detail="You don't have a Card")

        verify_card = (
            db.query(GcashCard)
            .filter(
                GcashCard.card_number == card.card_number,
                GcashCard.expiration_date == card.expiration_date,
                GcashCard.cvv == card.cvv
            )
            .first()
        )

        if not verify_card:
            raise HTTPException(status_code=404, detail="Card Info is not in the database.")

        if verify_card.balance < cash_amount.amount:
            raise HTTPException(status_code=400, detail="Insufficient card balance.")

        wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
        if not wallet:
            raise HTTPException(status_code=404, detail="Wallet not found")

        
        verify_card.balance -= cash_amount.amount
        wallet.balance += cash_amount.amount

        db.commit()
        db.refresh(wallet)
        db.refresh(verify_card)
        return wallet
