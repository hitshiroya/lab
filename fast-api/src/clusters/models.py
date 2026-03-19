from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ClusterModel(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(index=True,unique=True)
    owner : str
    org : str
    is_active : bool = Field(default=False)
    