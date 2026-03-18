from typing import Optional

from pydantic import BaseModel


class ClusterReq(BaseModel):
    name: str
    owner: str
    org: str
    isActive: bool


class ClusterResponse(BaseModel):
    id: Optional[int] = None
    name: str
    owner: str
    org: str
    isActive: bool
