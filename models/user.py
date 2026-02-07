from uuid import UUID
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
  '''
  Describes fields for a User entity
  '''
  first_name: str = Field(..., description="A user's first name", example="James")
  last_name: str = Field(..., description="A user's family name", example="Perih")
  age: int = Field(..., description="A user's age, in years", example=45)
  position: str = Field(..., description="The user's position within the organization", example="CEO")
  address: str = Field(..., description="The user's primary address", example="493 Queen Street")
  address_line2: str = Field(..., description="Optional additional address information", example="Suite 42")
  city: str = Field(..., description="User's city", example="Winnipeg")
  postal: str = Field(..., description="User's postal/zip code.", example="R3J 1L3")
  country: str = Field(..., description="User's country", example="Canada")

class User(UserCreate):
  '''
  A User entity
  '''
  id: UUID = Field(..., description="Unique ID")
