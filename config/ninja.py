from ninja import NinjaAPI, router
from apps.chats.views import router as chat_router
from apps.foruns.views.posts import router as post_router
from auth.router import router as auth_router
from apps.users.views.user import router_user
from apps.users.views.user_profile import router_profile

api = NinjaAPI(
    title="Ninja API",
    version="1.0.0"    
)

api.add_router("/auth", auth_router)
api.add_router("/users", router_user)
api.add_router("/profiles", router_profile)
api.add_router("/posts", post_router)
api.add_router("/chat", chat_router)

@api.get("/health", tags=["System"], auth=None)
def health(request):
    return {"status": "ok"}

