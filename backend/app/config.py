from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str
    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
