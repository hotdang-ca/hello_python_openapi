from pydantic import BaseModel, Field
from typing import Optional

class ItemCreate(BaseModel):
  name: str = Field(..., description="Item name", example="Laptop")
  price: float = Field(..., description="Item price", example=999.99)

class Item(ItemCreate):
  id: int = Field(..., description="Unique item ID")
  