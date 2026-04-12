from ninja import ModelSchema, Schema
from pydantic import Field
from datetime import datetime
from apps.user.models import Profile, User

class UserEmbed(ModelSchema):
    class Meta:
        model = User
        fields = ['id', 'email']
    
class ProfileEmbed(ModelSchema):
    class Meta:
        model = Profile
        fields = ['id', 'name']

class UserResponse(Schema):
    created_at: datetime
    updated_at: datetime
    active: bool
    user_id: int = Field(alias="pk")

    class Config:
        from_attributes = True
        populate_by_name = True

class ProfileResponse (Schema):
    pass
        

class CreateUserRequest(Schema):
    email: str
    password: str
