from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.clusters.db import create_db_and_table
from src.clusters.routes import cluster_router
from src.clusters.models import ClusterModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to db
    create_db_and_table()
    yield
    
    



app = FastAPI(lifespan=lifespan)

app.include_router(cluster_router, prefix="/api/v1")


