from ninja import NinjaAPI, router
from apps.chat.views import router as chat_router
from apps.forum.views.posts import router as post_router
from auth.router import router as auth_router
from apps.user.views.user import router_user
from apps.user.views.user_profile import router_profile
from django.conf import settings

api = NinjaAPI(
    title="API Além das Fronteiras",
    version="1.0.0",
    
    description="API para o projeto Além das Fronteiras, que visa conectar imigrantes a oportunidades de educação e integração social.",
)

api.add_router("/auth", auth_router)
api.add_router("/users", router_user)
api.add_router("/profiles", router_profile)
api.add_router("/posts", post_router)
api.add_router("/chat", chat_router)

@api.get("/health", tags=["System"], auth=None)
def health(request):
    return {"status": "ok"}

