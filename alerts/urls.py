from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import AlertViewSet

router = DefaultRouter()
router.register(r'', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
