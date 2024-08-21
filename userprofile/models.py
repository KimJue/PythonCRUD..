from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id
