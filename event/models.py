from django.db import models

from posts.models import Post


class Event(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
