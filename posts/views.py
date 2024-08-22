from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

import posts
from alerts.models import Alert
from posts.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment
from posts.services import PostService, CommentService
from userprofile.models import UserProfile


class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        # 1층
        title = request.data['title']
        content = request.data['content']
        user_id = request.data['user_id']

        # 2층 입구
        post = PostService.create_post(title=title, content=content, user_id=user_id)

        serialized_post = PostSerializer(post)
        # 1층
        return Response(serialized_post.data)

        # 나를 팔로우 하고 있는 사람들을 모두 찾아서, 그 사람들의 alert 테이블에 블로그 글이 작성됐다는 알림을 추가한다.
        # 나를 팔로우 하고 있는 사람들을 찾는 쿼리 SELECT * FROM

    # def create(self, request, *args, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # data = request.data

    #post = Post.objects.create(
    #   title=data['title'],
    #  content=data['content']
    # )

    #return Response(PostSerializer(post).data)


class PostDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'Error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(post).data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'Error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(PostSerializer(post).data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post is not None:
            post.delete()
            return Response({'삭제': True})

        return Response({"Error": True}, status=404)


class CommentAPI(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        return Response(CommentSerializer(comments, many=True).data)

    def post(self, request):
        post_id = request.data['post_id']
        content = request.data['content']
        author_id = request.data['author']

        # CommentService를 사용해 댓글 생성
        comment = CommentService.create_comment(post_id=post_id, content=content, author_id=author_id)

        serialized_comment = CommentSerializer(comment)
        return Response(serialized_comment.data, status=status.HTTP_201_CREATED)


class CommentDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def get(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({'error': 'Comment not found'}, status=404)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({'error': 'Comment not found'}, status=404)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({'error': 'Comment not found'}, status=404)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response({'error': 'Comment not found'}, status=404)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
