
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from src.auth.db import get_session
from src.auth.schemas import LoginReq, LoginResponse, RegisterReq, RegisterResponse
from src.auth.services import AuthService

auth_router = APIRouter(prefix="/auth", tags=["auth"])

SessionDep = Annotated[Session, Depends(get_session)]


@auth_router.post("/register",response_model=RegisterResponse,status_code=status.HTTP_201_CREATED)
async def register_user(user_register_data: RegisterReq, session:SessionDep):
    new_user = AuthService.register_user(user_register_data,session)
    return new_user


@auth_router.post("/login", response_model=LoginResponse,status_code=status.HTTP_200_OK)
async def login_user(user_login_data: LoginReq,session:SessionDep):
    user_logged_in = AuthService.login_user(user_login_data,session)
    if user_logged_in is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid username or password")
    
    return user_logged_in



