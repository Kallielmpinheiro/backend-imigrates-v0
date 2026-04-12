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
    
    
    protocal_number = models.CharField('Número do Protocolo', max_length=255, null=True, blank=True)
    visa_number = models.CharField('Número do Visto', max_length=255, null=True, blank=True)
    passport_number = models.CharField('Número do Passaporte', max_length=255, null=True, blank=True)
    
class ProfileDocument(BaseModel):
    
    TYPE_CHOICES = [
        
        ('birth_certificate', 'Certidão de Nascimento'),
        ('passport', 'Passaporte'),
        ('cover_letter', 'Carta de Apresentação'),
        
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = models.CharField('Tipo do Documento', max_length=255, choices=TYPE_CHOICES)
    document = models.FileField(upload_to='documents/')