from pydantic import BaseModel, Field
from datetime import datetime

# Item schemas
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, description="Item name cannot be empty")
    description: str | None = None
    price: float = Field(..., gt=0, description="Price must be positive")
    is_available: bool = True

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, description="Item name cannot be empty")
    description: str | None = None
    price: float | None = Field(None, gt=0, description="Price must be positive")
    is_available: bool | None = None

class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True
