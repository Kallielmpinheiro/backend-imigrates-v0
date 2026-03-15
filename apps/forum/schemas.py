from ninja import Schema

class CreateForumRequest(Schema):
    title: str
    content: str
    
class UpdateForumRequest(Schema):
    title: str
    content: str
    
class ForumResponse(Schema):
    id: int
    title: str
    content: str