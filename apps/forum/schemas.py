from datetime import datetime
from typing import Optional
from ninja import Schema, ModelSchema
from pydantic import ConfigDict, Field
from apps.forum.models import Post
from apps.user.schemas import UserEmbed, ProfileEmbed
from .models import Post, PostResponse

class postEmbed(ModelSchema):
    class Meta:
        model = Post
        exclude = ['imagem']
        
class FilePostResponse(Schema):
    url: str

class CreatePostRequest(Schema):
    title: str
    content: str
    category: str
    
class UpdatePostRequest(Schema):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    
class PostResponse(Schema):
    post_id: int = Field(alias="pk")
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    content: Optional[str] = None
    user: UserEmbed
    category: Optional[str] = None
    file: Optional[FilePostResponse] = None

    @staticmethod
    def resolve_file(obj) -> Optional[FilePostResponse]:
        if obj.imagem:
            return FilePostResponse(url=obj.imagem.url)
        return None

    @staticmethod
    def resolve_category(obj) -> Optional[str]:
        return str(obj.category) if obj.category is not None else None
    
    class Config:
        from_attributes = True
        populate_by_name = True
    

class PostResponseResponse(Schema):
    post_response_id : int = Field(alias="pk")
    created_at: datetime
    updated_at: datetime
    active: bool
    post: postEmbed
    user : UserEmbed
    response : str
    
    class Config:
        from_attributes = True
        populate_by_name = True
    
class CreatePostResponseRequest(Schema):
    response: str

class UpdatePostResponseRequest(Schema):
    response: str