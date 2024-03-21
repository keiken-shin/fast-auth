import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.models.user_model import User
from app.api.v1.router import router

logger = logging.getLogger(__name__)

"""
    Database initialization method
"""
async def init_db():
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).doer 
    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

"""
    Before the application starts up
    initialize needed services
"""
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
        Initialize application services
    """

    await init_db()

    yield

def create_app() -> FastAPI:
    logger.debug("Initializing App")
    app = FastAPI(
        lifespan=lifespan,
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    app.include_router(router, prefix=settings.API_V1_STR)

    return app