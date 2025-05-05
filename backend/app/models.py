from sqlmodel import SQLModel, Field
from fastapi_users_db_sqlmodel import SQLModelBaseUserDB
from typing import Optional
from datetime import date

class User(SQLModelBaseUserDB, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False

class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    name: str
    price: float
    currency: str = "EUR"
    billing_cycle: str = "monthly"
    next_renewal: date
    category: str | None = None
