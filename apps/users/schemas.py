from ninja import Schema
from pydantic import ConfigDict, Field
from datetime import datetime


class CreateUserRequest(Schema):
    email: str
    password: str

class UserResponse(Schema):

    created_at: datetime
    updated_at: datetime
    active: bool
    user_id: int = Field(alias="pk")

    class Config:
        from_attributes = True
        populate_by_name = True
        

