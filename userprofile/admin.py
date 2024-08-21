from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'password', 'email', )
    search_fields = ('user_id', )


admin.site.register(UserProfile, UserProfileAdmin)
