from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from userprofile.factories import UserProfileFactory


class QnACreationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserProfileFactory.create()
        self.client.force_authenticate(user=self.user)

    def test_create_qna_success(self):
        response = self.client.post('/qna/', {
            'user': self.user.user_id,
            'question': 'What is Django?',
            'answer': 'Django is a high-level Python web framework.',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['question'], 'What is Django?')
        self.assertEqual(response.data['answer'], 'Django is a high-level Python web framework.')

    def test_create_qna_invalid_data(self):
        response = self.client.post('/qna/', {
            'question': 'What is Django?',
        }, format='json')  # answer가 없어서 유효성 검사 실패

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('answer', response.data)