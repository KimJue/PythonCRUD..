from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from userprofile.factories import UserProfileFactory


class UserProfileTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserProfileFactory.create()  # 테스트용 사용자 생성
        self.client.force_authenticate(user=self.user)

    def test_유저프로필_생성_성공시(self):
        response = self.client.post('/userprofile/', {
            'user_id': 'new_user',
            'password': 'new_password',
            'email': 'new_user@example.com',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_id'], 'new_user')
        self.assertEqual(response.data['email'], 'new_user@example.com')

    def test_create_userprofile_invalid_data(self):
        response = self.client.post('/userprofile/', {
            'user_id': '',  # 빈 user_id로 인해 유효성 검사 실패
            'password': 'short',  # 너무 짧은 비밀번호
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('user_id', response.data)
        self.assertIn('password', response.data)

    def test_get_userprofile(self):
        response = self.client.get(f'/userprofile/{self.user.user_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user_id'], self.user.user_id)

    def test_update_userprofile_success(self):
        response = self.client.put(f'/userprofile/{self.user.user_id}/', {
            'password': 'updated_password',
            'email': 'updated_user@example.com',
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'updated_user@example.com')

    def test_delete_userprofile_success(self):
        response = self.client.delete(f'/userprofile/{self.user.user_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # 삭제된 사용자로 인한 조회 요청은 404 오류를 반환해야 합니다.
        response = self.client.get(f'/userprofile/{self.user.user_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)