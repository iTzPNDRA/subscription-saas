from sqlmodel import select
from .models import Subscription
from .database import get_session

def create_subscription(user_id: int, sub_data):
    with get_session() as session:
        sub = Subscription(user_id=user_id, **sub_data.dict())
        session.add(sub)
        session.commit()
        session.refresh(sub)
        return sub

def list_subscriptions(user_id: int):
    with get_session() as session:
        return session.exec(select(Subscription).where(Subscription.user_id == user_id)).all()
