from typing import Optional
from uuid import UUID

from app.schemas.user_schema import UserAuth
from app.models.user_model import User
from app.core.security import get_password, verify_password

class UserService:
    @staticmethod
    async def create(user: UserAuth):
        _user = User(
            username = user.username,
            email = user.email,
            password = get_password(user.password)
        ) 

        await _user.save()
        return _user
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        
        if not verify_password(password=password, hash=user.password):
            return None
        
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user
    
    @staticmethod
    async def get_user_by_id(id: UUID) -> Optional[User]:
        user = await User.find_one(User.user_id == id)
        return user