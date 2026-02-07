from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from uuid import uuid4

from models.item import Item, ItemCreate

app = FastAPI(
  title="Sample FastAPI /w OpenAPI",
  description="A sample API demonstrating classes, models, and automatic Swagger gen",
  version="1.0.0"
)

# in-memory store
ITEMS = []

@app.get("/items", response_model=List[Item])
def list_items(min_price: Optional[float] = Query(None, description="Min price filter")):
  """
  Get all items.

  Optionally filter items by minimum price.
  """
  if min_price is None:
    return ITEMS

  return [item for item in ITEMS if item["price"] >= min_price]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
  """
  Get item by ID
  
  :param item_id: ID of the item to fetch
  """
  for item in ITEMS:
    if item["id"] == item_id:
      return item
  
  raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
  """
  Create a new item.

  Adds an item to the system and returns it.
  """
  new_item = item.dict()
  new_item["id"] = str(uuid4())
  ITEMS.append(new_item)
  return new_item

@app.put("/items/{item_id}", response_model=Item, status_code=200)
def update_item(new_item: ItemCreate, item_id: str):
  """
  Updates an Item with specified ID
  
  :param new_item: The new item, in full
  :type new_item: ItemCreate
  :param item_id: The id for which item to update
  :type item_id: str
  """
  for i, item in enumerate(ITEMS):
    if item["id"] == item_id:
      updated_item = new_item.dict()
      updated_item["id"] = item_id
      ITEMS[i] = updated_item
      return updated_item
  
  raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=201) # 204 if i were absolutely smart about it
def delete_item(item_id: str):
  """
  Deletes an item.
  
  :param item_id: The item ID to delete.
  :type item_id: str
  """
  for i, item in enumerate(ITEMS):
    if item["id"] == item_id:
      ITEMS.pop(i)
      return {"message": f"Item {item_id} deleted successfully"}
  
  raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

