from ninja import Router
from apps.foruns.models import Post
from apps.foruns.schemas import CreatePostRequest, PostResponse
from apps.foruns.views.comment import router as comments_router
from apps.foruns.views.reply import router as replies_router

router = Router(tags=["Post"])

router.add_router("/comments", comments_router)

def health(request):
    return 200, {"status": "ok"}

@router.get('/', response={200: list[PostResponse], 404: dict})
def get_posts(request):
    try:
        posts = Post.objects.all()
        return 200, posts
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

@router.post('/', response={201: PostResponse, 401: dict}, summary="Criar post")
def create_post(request, payload: CreatePostRequest):
    
    post = Post(
        title=payload.title,
        content=payload.content,
    )
    post.save()
    
    return 201, PostResponse.from_orm(post)

@router.get('/{post_id}', response={200: PostResponse, 404: dict})
def get_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        return 200, post
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}

@router.put('/{post_id}', response={200: PostResponse, 404: dict})
def update_post(request, post_id: int, payload: CreatePostRequest):
    try:
        post = Post.objects.get(id=post_id)
        post.title = payload.title
        post.content = payload.content
        post.save()
        return 200, PostResponse.from_orm(post)
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}


@router.delete('/{post_id}', response={204: None, 404: dict})
def delete_post(request, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return 204, None
    except Post.DoesNotExist:
        return 404, {"detail": "Post não encontrado"}
