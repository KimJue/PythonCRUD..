from django.db import models

from userprofile.models import UserProfile


class Alert(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='alerts', null=True, blank=True)  # 기본값 설정 없음

    def __str__(self):
        return self.title

