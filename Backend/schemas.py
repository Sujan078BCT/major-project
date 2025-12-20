from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    email: Optional[str]

class UserResponse(User):
    access_token: str
    token_type: str
