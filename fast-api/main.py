from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.clusters.routes import cluster_router
from src.clusters.models import ClusterModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    
    
    



app = FastAPI(lifespan=lifespan)

app.include_router(cluster_router, prefix="/api/v1")


