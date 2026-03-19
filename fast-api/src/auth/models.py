from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class AuthModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username : str = Field(index=True,unique=True)
    name: str 
    email: str = Field(index=True,unique=True)
    password : str
    