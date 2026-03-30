from ninja import Router
from typing import List
from apps.foruns.schemas import CreateForumRequest, UpdateForumRequest, ForumResponse
from apps.foruns.models import Forum, Comment, Reply, LikeComment, LikeReply


router = Router()

# Create your views here.

#@router.get("/health", response={200: dict}, summary="Health check do forum")
def health(request):
    return 200, {"status": "ok"}


@router.get(
    "/",
    response={200: List[ForumResponse]},
    summary="Listar forums",
    operation_id="forum_list",
)
def list_forums(request):
    return 200, list(Forum.objects.filter(active=True).values('created_at', 'updated_at', 'title', 'description'))


@router.get(
    "/{id}",
    response={200: ForumResponse, 404: dict},
    summary="Buscar forum por ID",
    operation_id="forum_retrieve",
)
def get_forum(request, id: int):
    return 200, {}


@router.post(
    "/",
    response={201: ForumResponse, 422: dict},
    summary="Criar forum",
    operation_id="forum_create",
)
def create_forum(request, payload: CreateForumRequest):
    return 201, {}


@router.put(
    "/{id}",
    response={200: ForumResponse, 404: dict},
    summary="Atualizar forum",
    operation_id="forum_update",
)
def update_forum(request, id: int, payload: UpdateForumRequest):
    return 200, {}

@router.delete(
    "/{id}",
    response={204: None, 404: dict},
    summary="Deletar forum",
    operation_id="forum_delete",
)
def delete_forum(request, id: int):
    return 204, None
