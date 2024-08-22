from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from posts.views import PostAPI
from .views import UserProfileViewSet, UserFollowViewSet

router = SimpleRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register("follow", UserFollowViewSet, basename='follow')


urlpatterns = router.urls
