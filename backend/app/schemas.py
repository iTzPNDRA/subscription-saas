from datetime import date
from pydantic import BaseModel

class SubscriptionCreate(BaseModel):
    name: str
    price: float
    currency: str = "EUR"
    billing_cycle: str = "monthly"
    next_renewal: date
    category: str | None = None
