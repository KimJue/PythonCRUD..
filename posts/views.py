from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment

class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        try:
            title = request.data['title']
            content = request.data['content']
            author = request.UserProfile.objects.get(user_id=request.user_id)
            post = Post.objects.create(title=title, content=content, user_id=author)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        except KeyError as e:
            raise ValidationError({str(e):'This field is required.'})

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
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
