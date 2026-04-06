from datetime import datetime
from typing import Optional
from ninja import Schema
from pydantic import ConfigDict, Field

class CreatePostRequest(Schema):
    title: str
    content: str
    
class UpdatePostRequest(Schema):
    id: int
    title: Optional[str]
    content: Optional[str]

    
class PostResponse(Schema):

    created_at: datetime
    updated_at: datetime
    content: str
    post_id: int = Field(alias="pk")
    user_id : int
    
    class Config:
        from_attributes = True
        populate_by_name = True
    
class PostResponseResponse(Schema):

    created_at: datetime
    updated_at: datetime
    active: bool
    post_id : int
    user_id : int
    post_response_id : int = Field(alias="pk")
    response : str
    
    class Config:
        from_attributes = True
        populate_by_name = True
    
class CreatePostResponseRequest(Schema):
    response: str

class UpdatePostResponseRequest(Schema):
    response: str