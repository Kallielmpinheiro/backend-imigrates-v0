from django.contrib import admin
from apps.foruns.models import Comment, Forum, LikeComment, LikeReply, Post, Reply
# Register your models here.


class ForumAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')

admin.site.register(Forum, ForumAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(Post, PostAdmin)

    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(Comment, CommentAdmin)

    
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(Reply, ReplyAdmin)


class LikeCommentAdmin(admin.ModelAdmin): 
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(LikeComment, LikeCommentAdmin)

    
class LikeReplyAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(LikeReply, LikeReplyAdmin)
