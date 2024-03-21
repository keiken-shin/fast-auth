from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=25, description="user username")
    password: str = Field(..., min_length=5, max_length=25, description="user password")

class UserRes(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False