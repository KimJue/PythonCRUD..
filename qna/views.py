from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QnA
from .serializers import QnASerializer
from userprofile.models import UserProfile

class QnAListCreate(APIView):
    def get(self, request):
        qnas = QnA.objects.all()
        serializer = QnASerializer(qnas, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = UserProfile.objects.get(user_id=data['user_id'])  # 요청에서 사용자 ID를 가져옵니다.

        qna = QnA.objects.create(
            user=user,  # QnA를 생성한 사용자를 지정합니다.
            question=data['question'],
            answer=data['answer']
        )

        serializer = QnASerializer(qna)
        return Response(serializer.data, status=201)

class QnADetail(APIView):
    def get_object(self, pk):
        try:
            return QnA.objects.get(pk=pk)
        except QnA.DoesNotExist:
            return None

    def get(self, request, pk):
        qna = self.get_object(pk)
        if qna is None:
            return Response({'error': 'QnA not found'}, status=404)
        serializer = QnASerializer(qna)
        return Response(serializer.data)

    def put(self, request, pk):
        qna = self.get_object(pk)
        if qna is None:
            return Response({'error': 'QnA not found'}, status=404)
        serializer = QnASerializer(qna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        qna = self.get_object(pk)
        if qna is None:
            return Response({'error': 'QnA not found'}, status=404)
        serializer = QnASerializer(qna, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        qna = self.get_object(pk)
        if qna is None:
            return Response({'error': 'QnA not found'}, status=404)
        qna.delete()
        return Response(status=204)
