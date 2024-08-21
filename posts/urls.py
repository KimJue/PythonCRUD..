from django.urls import path
from .views import PostAPI, PostDetailAPI, CommentAPI, CommentDetailAPI

urlpatterns = [
    path('', PostAPI.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    path('comments/', CommentAPI.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailAPI.as_view(), name='comment-detail'),
]