from django.urls import path
from .views import PostAPI, PostDetailAPI, CommentAPI, CommentDetailAPI

urlpatterns = [
    path('', PostAPI.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    path('comment/', CommentAPI.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentDetailAPI.as_view(), name='comment-detail'),
]