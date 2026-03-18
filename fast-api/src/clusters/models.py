from typing import Optional
from sqlmodel import Field, SQLModel


class ClusterModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    owner : str
    org : str
    is_active : bool = Field(default=False)
    