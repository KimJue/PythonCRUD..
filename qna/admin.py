from django.contrib import admin
from .models import QnA


# Register the QnA model with the admin site
@admin.register(QnA)
class QnAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at')
    search_fields = ('question', 'answer')
