from django.contrib import admin
from .models import Alert


# Register the QnA model with the admin site
@admin.register(Alert)
class QnAAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'is_active')
