from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import User
from db import SessionLocal


router = APIRouter()


class UserRequest(BaseModel):
    email : str
    username : str
    first_name : str
    last_name : str
    role : str
    password : str
    is_active: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/auth/user")
async def create_user(db : db_dependency, create_user : UserRequest):
    user_model = User(
        email = create_user.email,
        username = create_user.username,
        first_name = create_user.first_name,
        last_name = create_user.last_name,
        role = create_user.role,
        hashed_password = create_user.password,
        is_active = create_user.is_active
    )
    db.add(user_model)
    db.commit()


# @router.get("/auth/users")
# async def get_all_users():
#     user_model = db.query(User).all()

#     return user_model


