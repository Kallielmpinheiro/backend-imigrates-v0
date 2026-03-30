from ninja import Router
from apps.foruns.schemas import CommentResponse, CreateCommentRequest, UpdateCommentRequest
from apps.foruns.views.reply import router as replies_router
from apps.foruns.models import Comment, Post

router = Router()

router.add_router("/replies", replies_router)

#@router.get("/health", response={200: dict}, summary="Health check dos comentários")
def health(request):
    return 200, {"status": "ok"}

@router.get('/', response={200: list[dict], 404: dict})
def get_comments(request):
    return 200, list(Comment.objects.filter(active=True).values('created_at', 'updated_at', 'content', 'post_id'))

@router.post('/', response={201: CommentResponse, 404: dict}, summary="Criar comentário")
def create_comment(request, payload: CreateCommentRequest):
    try:
        post = Post.objects.get(pk=payload.post_id)
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

    comment = Comment(
        content=payload.content,
        post=post,
        autor=None
    )
    comment.save()

    return 201, CommentResponse.from_orm(comment)
    
@router.get('/{id}', response={200: CommentResponse, 404: dict})
def get_comment(request, id: int):
    try:
        comment = Comment.objects.get(id=id, active=True)
        return 200, CommentResponse.from_orm(comment)
    except Comment.DoesNotExist:
        return 404, {"detail": "Comentário não encontrado"}

@router.put('/{id}', response={200: CommentResponse, 404: dict})
def update_comment(request, id: int, payload: UpdateCommentRequest):
    try:
        comment = Comment.objects.get(id=id, active=True)
        if payload.content:
            comment.content = payload.content
            comment.save()
            return 200, CommentResponse.from_orm(comment)
        else:
            return 422, {"detail": "Nenhum campo para atualizar"}
        
        
    except Comment.DoesNotExist:
        return 404, {"detail": "Comentário não encontrado"}

@router.delete('/{id}', response={204: None, 404: dict})
def delete_comment(request, id: int):
    try:
        comment = Comment.objects.get(id=id, active=True)
        comment.delete()
        return 204, None
    except Comment.DoesNotExist:
        return 404, {"detail": "Comentário não encontrado"}

