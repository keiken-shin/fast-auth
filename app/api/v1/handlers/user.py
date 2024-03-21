from fastapi import APIRouter, HTTPException, status
import pymongo

from app.schemas.user_schema import UserAuth, UserRes
from app.services.user_service import UserService

user_router = APIRouter()

@user_router.post(
    "/create", 
    summary="Create new user", 
    response_model=UserRes
)
async def create_user(data: UserAuth):
    try:
        return await UserService.create(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with email or username already exist"
        )