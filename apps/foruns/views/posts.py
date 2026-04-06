from ninja import Router
from apps.foruns.models import Post
from apps.foruns.schemas import CreatePostRequest, PostResponse
from apps.foruns.views.post_responses import router as responses_router
from auth.jwt import JWTAuth
from apps.users.models import User
from typing import List

router = Router(tags=["Post"])
router.add_router('/{post_id}/responses', responses_router)

def health(request):
    return 200, {"status": "ok"}

@router.get('', auth=JWTAuth(), response={200: List[PostResponse], 404: dict})
def get_posts(request):
    try:
        posts = Post.objects.all()
        return 200, posts
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

@router.post('', auth=JWTAuth(), response={201: PostResponse, 401: dict}, summary="Criar post")
def create_post(request, payload: CreatePostRequest):
    
    try:
        user = User.objects.get(pk=request.auth['sub'])
    except User.DoesNotExist:
        return 401, {"message": "User not found"}
    except Exception as e:
        return 401, {"message": "Invalid credentials"}
    
    post = Post(
        user=user,
        title=payload.title,
        content=payload.content,
    )
    post.save()
    
    return 201, PostResponse.from_orm(post)

@router.get('/{post_id}', auth=JWTAuth(), response={200: PostResponse, 404: dict})
def get_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        return 200, post
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

@router.put('/{post_id}', auth=JWTAuth(), response={200: PostResponse, 404: dict})
def update_post(request, post_id: int, payload: CreatePostRequest):
    try:
        post = Post.objects.get(id=post_id)
        post.title = payload.title
        post.content = payload.content
        post.save()
        return 200, PostResponse.from_orm(post)
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}


@router.delete('/{post_id}', auth=JWTAuth(), response={204: None, 404: dict})
def delete_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return 204, None
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}