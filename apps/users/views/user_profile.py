from django.db.models import F
from ninja import Router
from apps.users.models import User
from apps.users.schemas import CreateUserRequest, UserResponse
from auth.jwt import JWTAuth

# Create your views here.

router_profile = Router(tags=["Profile"])

# TODO definir

