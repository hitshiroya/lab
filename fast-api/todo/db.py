from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()
SQLALCHEMY_DATABASE_URL = 'DB_URL'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind = engine)

Base = declarative_base()

