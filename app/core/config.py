from decouple import config
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    # Server Settings
    port: int = config("PORT", cast=int)

    # CORS
    CORS_ORIGINs: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "DOER"

    # DATABASE
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)

    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str  = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str  = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7     # 7 days 
    ALGORITHM: str = "HS256"


    class Config:
        case_sensitive = True

settings = Settings()