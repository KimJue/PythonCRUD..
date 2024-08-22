from rest_framework import serializers
from posts.models import Post
from posts.models import Comment
from userprofile.models import UserProfile


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), write_only=True)
    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "title",
            "content",
            "created_at",
            "updated_at",
            "comments",
        )
