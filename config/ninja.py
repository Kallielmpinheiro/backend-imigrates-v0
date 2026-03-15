from ninja import NinjaAPI
from apps.chat.views import router as chat_router
from apps.forum.views import router as forum_router

api = NinjaAPI(
    title="Ninja API",
    version="1.0.0",
)

api.add_router("/chat/", chat_router)
api.add_router("/forum/", forum_router)

@api.get("/health", tags=["System"], auth=None)
def health(request):
    return {"status": "ok"}

