from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import subscriptions
from .auth import auth_router

app = FastAPI(title="Subscription Tracker API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
