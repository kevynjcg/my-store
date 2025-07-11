from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.db.models.card import Card
from src.db.models.card_list import GcashCard
from src.schemas.auth import Token
from src.schemas.card import CardCreate, CardRead
from src.db.models.user import User



class CardService:

    @staticmethod
    def create_card_for_user(user_id: int, card_data, db: Session):
        existing_card = db.query(Card).filter(Card.user_id == user_id).first()
        if existing_card:
            raise HTTPException(status_code=400, detail="User already has a card.")


        valid_card = db.query(GcashCard).filter(
            GcashCard.first_name == card_data.first_name,
            GcashCard.last_name == card_data.last_name,
            GcashCard.card_number == card_data.card_number,
            GcashCard.expiration_date == card_data.expiration_date,
            GcashCard.cvv == card_data.cvv

        ).first()

        if not valid_card:
            raise HTTPException(status_code=404, detail="Invalid card details. This card does not exist.")

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        new_card = Card(
            user_id=user_id,
            card_number=card_data.card_number,
            expiration_date=card_data.expiration_date,
            cvv=card_data.cvv,
            brand=card_data.brand,
            first_name=user.first_name,
            last_name=user.last_name,


        )
        db.add(new_card)
        db.commit()
        db.refresh(new_card)
        return new_card

    @staticmethod
    def get_card_for_user(user_id: int, db: Session):
        card = db.query(Card).filter(Card.user_id == user_id).first()
        if not card:
            raise HTTPException(status_code=404, detail="You don't have a Card")
        return card

    @staticmethod
    def update_card_for_user(user_id: int, card_data, db: Session):
        card = db.query(Card).filter(Card.user_id == user_id).first()
        if not card:
            raise HTTPException(status_code=404, detail="Card not found.")

        valid_card = db.query(GcashCard).filter(
            GcashCard.first_name == card_data.first_name,
            GcashCard.last_name == card_data.last_name,
            GcashCard.card_number == card_data.card_number,
            GcashCard.expiration_date == card_data.expiration_date,
            GcashCard.cvv == card_data.cvv

        ).first()

        if not valid_card:
            raise HTTPException(status_code=404, detail="Invalid card details. This card does not exist.")
        card.first_name = card_data.first_name
        card.last_name = card_data.last_name
        card.card_number = card_data.card_number
        card.expiration_date = card_data.expiration_date
        card.cvv = card_data.cvv
        card.brand = card_data.brand

        db.commit()
        db.refresh(card)
        return card

    @staticmethod
    def delete_card_for_user(user_id: int, db: Session):
        card = db.query(Card).filter(Card.user_id == user_id).first()
        if not card:
            raise HTTPException(status_code=404, detail="Card not found.")
        db.delete(card)
        db.commit()