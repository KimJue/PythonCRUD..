from django.db import models

from userprofile.models import UserProfile
from django.db import migrations, models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
