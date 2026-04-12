from ninja import Router, UploadedFile, Form, File
from ninja.files import UploadedFile
from apps.forum.models import Post
from apps.forum.schemas import CreatePostRequest, PostResponse, UpdatePostRequest
from apps.forum.views.post_responses import router as responses_router
from auth.jwt import JWTAuth
from apps.user.models import User
from typing import List
from django.db import transaction

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}

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
def create_post(request, payload: Form[CreatePostRequest], imagem: UploadedFile = File(None)):
    
    try:
        user = User.objects.get(pk=request.auth['sub'])
    except User.DoesNotExist:
        return 401, {"message": "User not found"}
    except Exception as e:
        return 401, {"message": "Invalid credentials"}
    
    if imagem is not None:
        if imagem.size > MAX_FILE_SIZE:
            return 422, {"message": "Imagem excede o limite de 5MB"}

        if imagem.content_type not in ALLOWED_TYPES:
            return 422, {"message": f"Tipo não permitido: {imagem.content_type}"}
        
    with transaction.atomic():
        try:
            post = Post(
                user=user,
                title=payload.title,
                content=payload.content,
                category=payload.category,
                imagem=imagem
            )
            post.save()
            
        except Exception as e:
            return 400, {"message": "Error creating post, rolling back transaction"}
    
    return 201, PostResponse.from_orm(post)

@router.get('/{post_id}', auth=JWTAuth(), response={200: PostResponse, 404: dict})
def get_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        return 200, post
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

@router.put('/{post_id}', auth=JWTAuth(), response={200: PostResponse, 404: dict})
def update_post(request, post_id: int, payload: Form[UpdatePostRequest], imagem: UploadedFile = File(None)):
    try:
        post = Post.objects.get(id=post_id)
        post.title = payload.title if payload.title is not None else post.title
        post.content = payload.content if payload.content is not None else post.content
        post.category = payload.category if payload.category is not None else post.category
        post.imagem = imagem if imagem is not None else post.imagem
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