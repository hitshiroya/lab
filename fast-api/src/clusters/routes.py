from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from src.clusters.data import cluster
from src.clusters.db import get_session
from src.clusters.schemas import ClusterReq, ClusterResponse
from src.clusters.service import ClusterService

cluster_router = APIRouter(prefix="/clusters", tags=["clusters"])


SessionDep = Annotated[Session, Depends(get_session)]

"""
Get all the clusters available inside infra
"""


@cluster_router.get("/", response_model=list[ClusterResponse], status_code=status.HTTP_200_OK)
async def get_root(session: SessionDep):
    return ClusterService.get_all_clusters(session)


"""
Get specific cluster available inside infra
"""


@cluster_router.get("/{cluster_id}", response_model=ClusterResponse, status_code=status.HTTP_200_OK)
async def get_specific_cluster(cluster_id: int, session: SessionDep):
    result = ClusterService.get_specific_cluster(cluster, cluster_id)

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
async def create_cluster_entry(clusterData: ClusterReq, session: SessionDep):
    return ClusterService.create_cluster_entry(cluster, clusterData)


"""
Update existing cluster with the new information inside infra data
"""


@cluster_router.put("/{cluster_id}", response_model=ClusterResponse, status_code=status.HTTP_200_OK)
async def update_cluster(cluster_id: int, cluster_update_data: ClusterReq, session: SessionDep):
    result = ClusterService.update_cluster_entry(cluster, cluster_id, cluster_update_data)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID does not exist within existing records.",
        )
    return result


"""
Delete the specific entry from the infra list
"""


@cluster_router.delete("/{cluster_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cluster(cluster_id: int, session: SessionDep):
    result = ClusterService.delete_cluster_entry(cluster, cluster_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given ID does not exist within existing records.",
        )
