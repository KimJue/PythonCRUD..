from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from alerts.serializers import AlertSerializer
from .models import UserProfile, UserFollow


class UserProfileSerializer(serializers.ModelSerializer):
    alerts = AlertSerializer(many=True, read_only=True)
    class Meta:
        model = UserProfile
        fields = ("name", "email", "password", "alerts")

class UserFollowSerializer(ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'
