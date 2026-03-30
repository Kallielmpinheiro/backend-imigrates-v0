from ninja import Router

from apps.foruns.models import Comment, Reply
from apps.foruns.schemas import  CreateReplyRequest, ReplyResponse, UpdateReplyRequest

router = Router()

def health(request):
    return 200, {"status": "ok"}

@router.get('/', response={200: list[dict], 404: dict})
def get_replies(request):
    return 200, list(Reply.objects.filter(active=True).values('created_at', 'updated_at', 'content', 'comment_id'))

@router.post('/', response={201: ReplyResponse, 404: dict}, summary="Criar resposta")
def create_reply(request, payload: CreateReplyRequest):
    
    try:
        comment = Comment.objects.get(pk=payload.comment_id)
    except Comment.DoesNotExist:
        return 404, {"detail": "Comentário não encontrado"}
    
    reply = Reply(
        content=payload.content,
        autor=None,
        comment_id=payload.comment_id
    )
    reply.save()
    
    return 201, ReplyResponse.from_orm(reply)

@router.get('/{id}', response={200: ReplyResponse, 404: dict})
def get_reply(request, id: int):
    try:
        reply = Reply.objects.get(id=id, active=True)
        return 200, ReplyResponse.from_orm(reply)
    except Reply.DoesNotExist:
        return 404, {"detail": "Resposta não encontrada"}

@router.put('/{id}', response={200: ReplyResponse, 404: dict})
def update_reply(request, id: int, payload: UpdateReplyRequest):

    
    try:
        reply = Reply.objects.get(id=id, active=True)
        if payload.content:
            reply.content = payload.content
            reply.save()
            return 200, dict(created_at=reply.created_at, updated_at=reply.updated_at, content=reply.content, comment_id=reply.comment_id)
        else:
            return 422, {"detail": "Nenhum campo para atualizar"}
        
        
    except Reply.DoesNotExist:
        return 404, {"detail": "Resposta não encontrada"}
    
    
@router.delete('/{id}', response={204: None, 404: dict})
def delete_reply(request, id: int):
    try:
        reply = Reply.objects.get(id=id, active=True)
        reply.delete()
        return 204, None
    except Reply.DoesNotExist:
        return 404, {"detail": "Resposta não encontrada"}
