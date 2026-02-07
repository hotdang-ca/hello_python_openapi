from fastapi import FastAPI, Query
from typing import List, Optional
from models import Item, ItemCreate

app = FastAPI(
  title="Sample FastAPI /w OpenAPI",
  description="A sample API demonstrating classes, models, and automatic Swagger gen",
  version="1.0.0"
)

# in-memory store
ITEMS = []

@app.get("/items", response_model=List[Item])
def get_items(min_price: Optional[float] = Query(None, description="Min price filter")):
  """
  Get all items.

  Optionally filter items by minimum price.
  """
  if min_price is None:
    return ITEMS

  return [item for item in ITEMS if item["price"] >= min_price]

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
  """
  Create a new item.

  Adds an item to the system and returns it.
  """
  new_item = item.dict()
  new_item["id"] = len(ITEMS) + 1
  ITEMS.append(new_item)
  return new_item
