from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from uuid import uuid4

from models.item import Item, ItemCreate
from models.user import User, UserCreate

app = FastAPI(
  title="Sample FastAPI /w OpenAPI",
  description="A sample API demonstrating classes, models, and automatic Swagger gen",
  version="1.0.0",
  root_path="/api"
)

# in-memory store
ITEMS = []
USERS = []

@app.get("/users", response_model=List[User], tags=["Users"])
def list_users():
  """
  Get all users
  """

  return USERS

@app.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: str):
  """
  Get user by ID
  
  :param user_id: User ID of user to search
  :type user_id: str
  """
  for user in USERS:
    if user["id"] == user_id:
      return user
  
  raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", response_model=User, status_code=201, tags=["Users"], description="Creates a new user")
def create_user(user: UserCreate):
  """
  Create a new user
  
  :param user: Description
  :type user: UserCreate
  """
  new_user = user.dict()
  new_user["id"] = str(uuid4())
  USERS.append(new_user)
  return new_user

@app.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: str, new_user: UserCreate):
  """
  Updates an existing user, by ID
  
  :param user_id: User ID to update
  :type user_id: str
  :param user: New User fields
  :type user: UserCreate
  """
  for u, user in enumerate(USERS):
    if user["id"] == user_id:
      updated_user = new_user.dict()
      updated_user["id"] = user_id
      USERS[u] = updated_user
      return updated_user
  
  raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=201, tags=["Users"])
def delete_user(user_id: str):
  """
  Deletes a user
  
  :param user_id: UserID belonging to user to delete
  :type user_id: str
  """
  for u, user in enumerate(USERS):
    if user["id"] == user_id:
      USERS.pop(u)
      return {"message": f"User {user_id} deleted successfully"}
  
  raise HTTPException(status_code=404, detail=f"User {user_id} not found")

@app.get("/items", response_model=List[Item], tags=["Items"])
def list_items(min_price: Optional[float] = Query(None, description="Min price filter")):
  """
  Get all items.

  Optionally filter items by minimum price.
  """
  if min_price is None:
    return ITEMS

  return [item for item in ITEMS if item["price"] >= min_price]

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: str):
  """
  Get item by ID
  
  :param item_id: ID of the item to fetch
  """
  for item in ITEMS:
    if item["id"] == item_id:
      return item
  
  raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201, tags=["Items"])
def create_item(item: ItemCreate):
  """
  Create a new item.

  Adds an item to the system and returns it.
  """
  new_item = item.dict()
  new_item["id"] = str(uuid4())
  ITEMS.append(new_item)
  return new_item

@app.put("/items/{item_id}", response_model=Item, status_code=200, tags=["Items"])
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

@app.delete("/items/{item_id}", status_code=201, tags=["Items"]) # 204 if i were absolutely smart about it
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

