from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from src.clusters.db import get_session
from src.clusters.schemas import ClusterReq, ClusterResponse
from src.clusters.service import ClusterService
from src.auth.dependencies import get_current_user

cluster_router = APIRouter(prefix="/clusters", tags=["clusters"])


SessionDep = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[dict, Depends(get_current_user)]

"""
Get all the clusters available inside infra
"""


@cluster_router.get("/", response_model=list[ClusterResponse], status_code=status.HTTP_200_OK)
async def get_root(session: SessionDep):
    return ClusterService.get_all_clusters(session)


"""
Get specific cluster available inside infra
"""


@cluster_router.get("/{cluster_name}", response_model=ClusterResponse, status_code=status.HTTP_200_OK)
async def get_specific_cluster(cluster_name: str, session: SessionDep):
    result = ClusterService.get_specific_cluster(cluster_name, session)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID does not exist within existing records.",
        )
    return result


"""
Add new cluster entry to infra data
"""


@cluster_router.post("/", response_model=ClusterResponse, status_code=status.HTTP_201_CREATED)
async def create_cluster_entry(clusterData: ClusterReq, session: SessionDep, current_user: CurrentUser):
    return ClusterService.create_cluster_entry(clusterData,session)


"""
Update existing cluster with the new information inside infra data
"""


@cluster_router.put("/{cluster_name}", response_model=ClusterResponse, status_code=status.HTTP_200_OK)
async def update_cluster(cluster_name: str, cluster_update_data: ClusterReq, session: SessionDep,current_user: CurrentUser):
    result = ClusterService.update_cluster_entry(cluster_name, cluster_update_data,session)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID does not exist within existing records.",
        )
    return result


"""
Delete the specific entry from the infra list
"""


@cluster_router.delete("/{cluster_name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cluster(cluster_name: str, session: SessionDep,current_user: CurrentUser):
    result = ClusterService.delete_cluster_entry(cluster_name,session)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID does not exist within existing records.",
        )
