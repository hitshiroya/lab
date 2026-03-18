from sqlmodel import Session, SQLModel, create_engine

from src.core.config import settings

engine = create_engine(settings.database_url)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session