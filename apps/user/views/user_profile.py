from django.db.models import F
from ninja import Router
from apps.user.models import User
from apps.user.schemas import CreateUserRequest, UserResponse
from auth.jwt import JWTAuth

# Create your views here.

router_profile = Router(tags=["Profile"])

# TODO definir

