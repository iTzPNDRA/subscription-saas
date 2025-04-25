from fastapi import APIRouter, Depends
from typing import List
from ..schemas import SubscriptionCreate
from ..crud import create_subscription, list_subscriptions
from ..auth import current_active_user

router = APIRouter()

@router.post("/", status_code=201)
def add_subscription(payload: SubscriptionCreate, user=Depends(current_active_user)):
    return create_subscription(user.id, payload)

@router.get("/", response_model=List[dict])
def get_subscriptions(user=Depends(current_active_user)):
    return list_subscriptions(user.id)
