from django.urls import path
from .views import QnAListCreate, QnADetail

urlpatterns = [
    path('', QnAListCreate.as_view(), name='qna-list-create'),
    path('<int:pk>/', QnADetail.as_view(), name='qna-detail'),
]