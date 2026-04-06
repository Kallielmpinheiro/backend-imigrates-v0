from ninja import Router
from apps.foruns.schemas import  CreatePostResponseRequest, PostResponseResponse, UpdatePostResponseRequest
from apps.foruns.models import Post, PostResponse
from apps.users.models import User
from auth.jwt import JWTAuth
from typing import List
from django.db import transaction

router = Router()

def health(request):
    return 200, {"status": "ok"}

@router.get('', auth=JWTAuth(), response={200:List[PostResponseResponse], 404: dict})
def get_responses(request):
    responses = PostResponse.objects.all()
    return 200, responses

@router.post('', auth=JWTAuth(), response={201: dict, 400: dict, 401: dict, 404: dict})
def create_response(request, payload: CreatePostResponseRequest):
    
    # fix para propragar o post_id para o router filho
    post_id = request.resolver_match.kwargs.get('post_id')
    
    try:
        user = User.objects.get(pk=request.auth['sub'])
    except User.DoesNotExist:
        return 401, {"message": "User not found"}

    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return 404, {"message": "Post not found"}

    with transaction.atomic():
        try:
            response = PostResponse(post=post, user=user, response=payload.response)
            response.save()
        except Exception as e:
            return 400, {"message": "Error creating response"}

    return 201, {"message": "Reply created"}

@router.get('/{response_id}', auth=JWTAuth(), response={200:PostResponseResponse, 404: dict})
def get_response(request, response_id: int):
    
    try:
        response = PostResponse.objects.get(pk=response_id)
    except PostResponse.DoesNotExist:
        return 404, {"message": "Response not found"}
    
    return 200, response

@router.put('/{response_id}', auth=JWTAuth(), response={200:PostResponseResponse, 404: dict})
def update_response(request, response_id: int, payload: UpdatePostResponseRequest):
    
    try:
        response = PostResponse.objects.get(pk=response_id)
    except PostResponse.DoesNotExist:
        return 404, {"message": "Response not found"}
    
    response.response = payload.response
    with transaction.atomic():
        try:
            response.save()
        except Exception as e:
            print(e)
            return 400, {"message": "Error updating response"}
        response.save()
    
    return 200, response

@router.delete('/{response_id}',auth=JWTAuth(), response={204: None, 404: dict})
def delete_response(request, response_id: int):
    try:
        response = PostResponse.objects.get(pk=response_id)
    except PostResponse.DoesNotExist:
        return 404, {"message": "Response not found"}
    with transaction.atomic():
        try:
            response.delete()
        except Exception as e:
            print(e)
            return 400, {"message": "Error deleting response"}
    return 204, None