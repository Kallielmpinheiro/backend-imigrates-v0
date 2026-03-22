from django.contrib import admin

from apps.users.models import Profile, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)