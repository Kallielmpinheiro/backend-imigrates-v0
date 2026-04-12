from ninja import Schema

class CreateChatRequest(Schema):
    imigrante_id: int
    voluntario_id: int
    
class ChatResponse(Schema):
    link: str
   

class UpdateChatRequest(Schema):
    pass