from fastapi import APIRouter, Depends, HTTPException
from src.db.session import get_db, SessionLocal, engine
from sqlalchemy.orm import Session
from src.schemas.card import CardCreate, CardRead, CardSafeRead, CardUpdate
from src.services.card_service import CardService
from src.core.security import get_admin_user, get_current_user
from src.db.models.card import Card


cards = APIRouter()

@cards.post("/add-card", response_model=CardRead)
def create_card(
    card_data: CardCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    created_card = CardService.create_card_for_user(user_id=current_user.id, card_data=card_data, db=db)
    return created_card

@cards.get("/my-card", response_model=CardSafeRead)
def get_my_card(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    my_card = CardService.get_card_for_user(user_id=current_user.id, db=db)
    return CardSafeRead.from_orm(my_card)

@cards.put("/update-card", response_model=CardSafeRead)
def update_my_card(
    card_data: CardUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated_card = CardService.update_card_for_user(user_id=current_user.id, card_data=card_data, db=db)
    return updated_card

@cards.delete("/", status_code=204)
def delete_my_card(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    CardService.delete_card_for_user(user_id=current_user.id, db=db)
    return None