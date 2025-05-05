from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr


# ---------- User ----------
class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_superuser: bool


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# ---------- Subscription ----------
class SubscriptionCreate(BaseModel):
    name: str
    price: float
    currency: str = "EUR"          # optional: ISO-Code
    billing_cycle: str = "monthly" # monthly | yearly | custom
    next_renewal: date
    category: Optional[str] = None
