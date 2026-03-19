from uuid import UUID

from pydantic import BaseModel


class RegisterReq(BaseModel):
    name: str
    username: str
    password: str
    email: str

class LoginReq(BaseModel):
    username: str
    password: str


class RegisterResponse(BaseModel):
    id: UUID
    name: str
    username: str
    email: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class LoginResponse(TokenResponse):
    username: str
    