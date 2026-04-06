from typing import List
from django.db.models import F
from ninja import Router
from apps.users.models import User
from apps.users.schemas import CreateUserRequest, UserResponse
from auth.jwt import JWTAuth
from django.shortcuts import get_object_or_404
from django.db import transaction, IntegrityError

# Create your views here.

router_user = Router(tags=["User"])

def health(request):
     return 200, {"status": "ok"}
 
@router_user.get('/', auth=JWTAuth(), response={200: List[UserResponse], 401: dict})
def list_users(request):
    users = User.objects.filter(active=True)
    return 200, users

@router_user.post('', auth=None, response={201: dict, 400: dict})
def create_user(request, payload: CreateUserRequest):
    
    user = User(
        email=payload.email,
        password=payload.password
    )
    
    if User.objects.filter(email=payload.email).exists():
        return 400, {"message": "Email already exists"}
    
    with transaction.atomic():    
        try:
            user.save()
        except Exception as e:
            return 400, {"message": "Error creating user"}
        
    return 201, {"message": "User created"}

@router_user.get('/{user_id}', auth=JWTAuth(), response={200: UserResponse, 401: dict})
def get_user(request, user_id: int):
    user = get_object_or_404(User, pk=user_id)
    return 200, user