from django.test import TestCase
from .factories import UserProfileFactory
from .models import UserProfile


class UserProfileTests(TestCase):
    def setUp(self):
        self.user_profile = UserProfileFactory.create()

    def test_유저_프로필_만들기(self):
        username = "test"
        created_user = UserProfileFactory.create(username=username)
        self.assertTrue(UserProfile.objects.filter(username=username).exists())
        # self.assertTrue(UserProfile.objects.exists())
        self.assertEqual(username, created_user.user.username)

    def test_select_related_사용(self):
        user_profile = UserProfile.objects.select_related('user').get(id=self.user_profile.id)
        self.assertEqual(user_profile.user.username, self.user_profile.user.username)
