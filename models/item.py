from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class ItemCreate(BaseModel):
  name: str = Field(..., description="Item name", example="Laptop")
  price: float = Field(..., description="Item price", example=999.99)

class Item(ItemCreate):
  id: UUID = Field(..., description="Unique item ID")
  