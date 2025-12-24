from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=1, description="Username cannot be empty")
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")

class UserUpdate(BaseModel):
    username: str | None = Field(None, min_length=1, description="Username cannot be empty")
    email: EmailStr | None = None
    full_name: str | None = None
    password: str | None = Field(None, min_length=6, description="Password must be at least 6 characters")

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime  | None = None
    
    class Config:
        from_attributes = True

class UserInDB(User):
    hashed_password: str

# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None 