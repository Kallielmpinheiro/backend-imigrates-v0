from django.db import models
from config.base_modal import BaseModel

# Create your models here.

class User(BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    cpf = models.CharField('CPF', max_length=14, null=True, blank=True)
    mobile = models.CharField('Celular', max_length=20, null=True, blank=True) 
    
    
class ProfileDocument(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField('Tipo do Documento', max_length=255)
    document = models.FileField(upload_to='documents/')