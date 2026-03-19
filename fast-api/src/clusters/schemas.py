from uuid import UUID

from pydantic import BaseModel


class ClusterReq(BaseModel):
    name: str
    owner: str
    org: str
    is_active: bool


class ClusterResponse(BaseModel):
    id: UUID
    name: str
    owner: str
    org: str
    is_active: bool
