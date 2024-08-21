from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import QnA
from .serializers import QnASerializer


class QnAListCreate(APIView):
    def get(self, request):
        qnas = QnA.objects.all()
        serializer = QnASerializer(qnas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QnASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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