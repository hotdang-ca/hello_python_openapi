from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class ItemCreate(BaseModel):
  name: str = Field(..., description="Item name", example="Laptop")
  price: float = Field(..., description="Item price", example=999.99)

class Item(ItemCreate):
  id: UUID = Field(..., description="Unique item ID", example="9e1c2b52-dd9f-4680-adf7-8d51fa1868af")
  