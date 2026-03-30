from datetime import datetime
from typing import Optional

from ninja import Schema
from pydantic import ConfigDict

class CreateForumRequest(Schema):
    title: str
    content: str
    
class UpdateForumRequest(Schema):
    title: str
    content: str
    
class ForumResponse(Schema):
    created_at: datetime
    updated_at: datetime
    title: str
    description: str
    
class CreatePostRequest(Schema):
    title: str
    content: str
    
    
class UpdatePostRequest(Schema):
    id: int
    title: Optional[str]
    content: Optional[str]
    
    
class PostResponse(Schema):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    title: str
    content: str
    
class CreateCommentRequest(Schema):
    content: str
    post_id: int
    
class UpdateCommentRequest(Schema):
    content: str
    
class CommentResponse(Schema):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    content: str
    post_id: int
    
class CreateReplyRequest(Schema):
    content: str
    comment_id: int
    
class UpdateReplyRequest(Schema):
    content: str
    
class ReplyResponse(Schema):
    model_config = ConfigDict(from_attributes=True)

    created_at: datetime
    updated_at: datetime
    content: str
    comment_id: int