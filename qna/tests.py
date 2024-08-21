from django.test import TestCase
from .factories import QnAFactory
from .models import QnA

class QnATests(TestCase):
    def setUp(self):
        self.qna = QnAFactory.create()

    def test_qna_만들기(self):
        self.assertTrue(QnA.objects.exists())
        self.assertEqual(self.qna.question, self.qna.question)

    def test_qna_answer_답변보유(self):
        self.assertTrue(self.qna.answer)
