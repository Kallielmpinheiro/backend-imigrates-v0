from django.contrib import admin

from apps.chat.models import Chat

# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatAdmin)
