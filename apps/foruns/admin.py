from django.contrib import admin
from apps.foruns.models import Post, PostResponse

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')

admin.site.register(Post, PostAdmin)

class PostResponseAdmin(admin.ModelAdmin):
    list_display = ('id','active','created_at', 'updated_at')
    
admin.site.register(PostResponse, PostResponseAdmin)