import jwt
from datetime import datetime, timedelta
from django.conf import settings
from ninja.security import HttpBearer

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "type": "access",
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=7),
        "type": "refresh",
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


class JWTAuth(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            payload = decode_token(token)
            if payload.get("type") != "access":
                return None
            return payload 
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None