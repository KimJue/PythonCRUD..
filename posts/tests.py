# 유닛테스트 unittest
#
# test1 posts 목록 조회 시 정상 데이터를 응답한다.
# test2 posts 생성 시 정상적으로 데이터가 생성된다.
# test3 posts 생성 시 잘못된 데이터를 전달하면 400 에러가 발생한다.
# test4 posts 생성 시 dbenv 발생하면 500 에러가 발생한다.


from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from userprofile.factories import UserProfileFactory
from .factories import PostFactory, CommentFactory


class Post_목록_조회_시(TestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserProfileFactory()
        PostFactory.create_batch(10, user=self.user)

    def test_정상_요청_시(self):
        with self.assertNumQueries(1):
            response = self.client.get(path="posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_요청_실패_시(self):
        # 1. 잘못된 URL로 요청
        response = self.client.get(path="/invalid-url/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # 2. 잘못된 HTTP 메서드로 요청 (POST 요청)
        response = self.client.post(path="/posts/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#def tearDown(self):
#   Post.objects.all().delete()
# class Post_생성_시(TestCase):
#   client = APIClient
#
#   def test_정상_요청_시(self): ...
#
#   def test_잘못된_데이터_전달_시(self): ...
