from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.auth.routes import auth_router
from src.clusters.routes import cluster_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(cluster_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")
