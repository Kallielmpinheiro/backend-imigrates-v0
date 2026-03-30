from ninja import NinjaAPI
from apps.chats.views import router as chat_router
from apps.foruns.views.post import router as post_router

api = NinjaAPI(
    title="Ninja API",
    version="1.0.0"    
)

api.add_router("/chat/", chat_router)
api.add_router("/posts/", post_router)

@api.get("/health", tags=["System"], auth=None)
def health(request):
    return {"status": "ok"}

