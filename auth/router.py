from ninja import Router
from ninja.errors import HttpError
from .jwt import create_access_token, create_refresh_token, decode_token
from .schemas import LoginSchema, TokenSchema, RefreshSchema
from apps.users.models import User

router = Router(tags=["Auth"])

@router.post("/login", response=TokenSchema, auth=None)
def login(request, payload: LoginSchema):
    try:
        user = User.objects.get(email=payload.email)
    except User.DoesNotExist:
        return 404, {"message": "User not found"}
    except Exception:
        return 401, {"message": "Invalid credentials"}
    
    if user.password != payload.password:
        return 401, {"message": "Invalid credentials"}
    
    return TokenSchema(
        access=create_access_token(user.pk),
        refresh=create_refresh_token(user.pk),
    )

@router.post("/refresh", response={200:TokenSchema, 401: dict}, auth=None)
def refresh(request, data: RefreshSchema):
    try:
        payload = decode_token(data.refresh)
        if payload.get("type") != "refresh":
            raise HttpError(401, "Token inválido")

        user_id = int(payload["sub"])

        return TokenSchema(
            access=create_access_token(user_id),
            refresh=create_refresh_token(user_id),
        )
    except Exception as e:
        print(e)
        return 401, {"message": "Refresh token inválido ou expirado"}