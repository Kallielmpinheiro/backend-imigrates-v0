from ninja import Router
from ninja.responses import Response
from typing import List
from apps.chat.schemas import CreateChatRequest, UpdateChatRequest, ChatResponse

router = Router(tags=["Chat"])

#@router.get("/health", response={200: dict}, summary="Health check do chat")
def health(request):
    return 200, {"status": "ok"}

@router.get(
    "/",
    response={200: List[ChatResponse]},
    summary="Listar chats",
    operation_id="chat_list",
)
def list_chats(request):
    return 200, []

@router.get(
    "/{id}",
    response={200: ChatResponse, 404: dict},
    summary="Buscar chat por ID",
    operation_id="chat_retrieve",
)
def get_chat(request, id: int):
    return 200, {}


@router.post(
    "/",
    response={201: ChatResponse, 422: dict},
    summary="Criar chat",
    operation_id="chat_create",
)
def create_chat(request, payload: CreateChatRequest):
    return 201, {}


@router.put(
    "/{id}",
    response={200: ChatResponse, 404: dict},
    summary="Atualizar chat",
    operation_id="chat_update",
)
def update_chat(request, id: int, payload: UpdateChatRequest):
    return 200, {}


@router.delete(
    "/{id}",
    response={204: None, 404: dict},
    summary="Deletar chat",
    operation_id="chat_delete",
)
def delete_chat(request, id: int):
    return 204, None