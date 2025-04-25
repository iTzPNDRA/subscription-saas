from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager

engine = create_engine("sqlite:///./subscriptions.db", connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_session():
    with Session(engine) as session:
        yield session
