from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostSerializer  #오류가 나서 serializers.py에서 PostSerializer 클래스를 정의하고 상속받음 !!
from posts.models import Post

from posts.serializers import CommentSerializer
from posts.models import Comment



class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response(PostSerializer(posts, many=True).data)

    def post(self, request):
        data = request.data

        post = Post.objects.create(
            title=data['title'],
            content=data['content']
        )

        return Response(PostSerializer(post).data)


class PostDetailAPI(APIView):
    def get_object(self, pk):  # try-except 구문을 사용하여 예외 처리
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:  # pk 값에 해당하는 포스트가 데이터베이스에 없는 경우
            return None

    def get(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)  # 위에 정의한 get_object 메소드를 사용하여 주어진 pk 값을 가진 포스트 객체를 가져옴 --> 패스파라미터
        if post is None:
            return Response({'Error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():  # 유효성 검사 유효하지 않을 경우 39번째 줄 오류담김  ( Boolean 값 )
            serializer.save()  # 유효할 경우 DB저장!
            return Response(PostSerializer(post).data)
        return Response(serializer.errors)

    def patch(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response({'Error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data, partial=True)  # partial=True 옵션을 주어 부분 업데이트를 허용함 !
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


