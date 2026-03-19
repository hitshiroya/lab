from sqlmodel import select

from src.auth.models import AuthModel
from src.core.security import create_access_token, hash_password, verify_password


class AuthService:
    @staticmethod
    def register_user(user_register_data,session):
        hashed_password = hash_password(user_register_data.password)
        new_user = AuthModel(name=user_register_data.name,username=user_register_data.username,email=user_register_data.email,password=hashed_password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    @staticmethod
    def login_user(user_login_data,session):
        user_exist = session.exec(select(AuthModel).where(AuthModel.username == user_login_data.username )).first()
        if not user_exist or not verify_password(user_login_data.password, user_exist.password):
            return None
        access_token = create_access_token(data={"sub": user_exist.username})
        return {"access_token": access_token, "token_type": "bearer", "username": user_exist.username}