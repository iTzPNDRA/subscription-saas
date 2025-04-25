from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str
    price: float
    currency: str = "EUR"
    billing_cycle: str = "monthly"
    next_renewal: date
    category: str | None = None
