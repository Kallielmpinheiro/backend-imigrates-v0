from datetime import datetime

from ninja import Schema

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