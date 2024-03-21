import bcrypt
from datetime import datetime, timezone, timedelta
from typing import Union, Any
from jose import jwt

from app.core.config import settings

# Encryption JWT
def create_access_token(subject: Union[str, Any], expires_delta: int = None):
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) * expires_delta
    else: 
        expires_delta = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None):
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) * expires_delta
    else: 
        expires_delta = datetime.now(timezone.utc) + timedelta(settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
    
    return encoded_jwt

# Encryption Password
def get_password(password: str) -> str:
    # Converting password string to array of bytes
    bytes = password.encode("utf-8")
    # Generate the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    return bcrypt.hashpw(bytes, salt)

def verify_password(password: str, hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), hash.encode())