from django.db import models
from userprofile.models import UserProfile


class QnA(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='qnas')  # 외래키 추가
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
