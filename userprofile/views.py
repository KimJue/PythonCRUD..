from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, UserFollow
from .serializers import UserProfileSerializer, UserFollowSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserFollowViewSet(ModelViewSet):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
