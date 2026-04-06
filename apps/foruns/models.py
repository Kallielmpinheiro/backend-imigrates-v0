from django.db import models
from apps.users.models import User
from config.base_modal import BaseModel

# Create your models here.
    
class Post(BaseModel):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField('Título', max_length=255)
    content = models.TextField('Conteúdo')
    imagem = models.ImageField(upload_to='post_images/', null=True, blank=True) # retirar null e blank depois de fechar com os requisitos
    
    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ['-created_at']
        
class PostResponse(BaseModel):

    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    response = models.TextField('Resposta')
    
    class Meta:
        verbose_name = "Resposta a Postagem"
        verbose_name_plural = "Respostas as Postagens"
        ordering = ['-created_at']