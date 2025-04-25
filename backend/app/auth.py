from fastapi import APIRouter

auth_router = APIRouter()

def current_active_user():
    class DummyUser:
        id = 1
    return DummyUser()
