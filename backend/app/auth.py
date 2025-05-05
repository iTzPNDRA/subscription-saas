from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from fastapi_users_db_sqlmodel import SQLModelUserDatabase
from .models import User
from .database import get_session
from .config import settings
from .schemas import UserRead, UserCreate         # ➊  SCHEMAS importieren

# ---------- DB helper ----------
def get_user_db():
    with get_session() as session:
        yield SQLModelUserDatabase(session, User)

# ---------- Auth backend ----------
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=60 * 60 * 24)

cookie_transport = CookieTransport(cookie_name="subscription_auth", cookie_max_age=60 * 60 * 24)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_db,
    [auth_backend],
)

auth_router = APIRouter()

# ➋  SCHEMAS an die Router-Fabriken übergeben
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend, UserRead),
    prefix="/auth/jwt",
    tags=["auth"],
)

current_active_user = fastapi_users.current_user(active=True)
