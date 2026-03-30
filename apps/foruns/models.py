from django.db import models
from apps.users.models import User
from config.base_modal import BaseModel

# Create your models here.

class Forum(BaseModel):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='forum_images/', null=True, blank=True)
    
    class Meta:
        verbose_name = "Fórum"
        verbose_name_plural = "Fóruns"
        ordering = ['-created_at']
    
    
class Post(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # retirar null e blank depois de implementar autenticação
    title  = models.CharField(max_length=255)
    content = models.TextField()
    imagem = models.ImageField(upload_to='post_images/', null=True, blank=True) # retirar null e blank depois de fechar com os requisitos
    
    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ['-created_at']

    @property
    def replies(self):
        return Reply.objects.filter(comment__post=self).count()            
    
class Comment(BaseModel):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # retirar null e blank depois de implementar autenticação
    content = models.TextField()
    
    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
        ordering = ['-created_at']
        
    

class Reply(BaseModel):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # retirar null e blank depois de implementar autenticação
    content = models.TextField()
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        ordering = ['-created_at']
    
class LikeComment(BaseModel):
    
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # retirar null e blank depois de implementar autenticação

    class Meta:
        verbose_name = "Like de Comentário"
        verbose_name_plural = "Likes de Comentários"
        ordering = ['-created_at']

class LikeReply(BaseModel):
    
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # retirar null e blank depois de implementar autenticação
    
    class Meta:
        verbose_name = "Like de Resposta"
        verbose_name_plural = "Likes de Respostas"
        ordering = ['-created_at']