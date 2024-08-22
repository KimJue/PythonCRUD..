from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import UserProfile, UserFollow


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserFollowSerializer(ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'
