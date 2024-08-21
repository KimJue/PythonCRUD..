from django.test import TestCase
from .factories import PostFactory, CommentFactory
from .models import Post, Comment

class PostTests(TestCase):
    def setUp(self):
        self.post = PostFactory.create()
        self.comments = [CommentFactory.create(post=self.post) for _ in range(3)]

    def test_post_만들기(self):
        self.assertTrue(Post.objects.exists())
        self.assertEqual(self.post.title, self.post.title)

    def test_post_with_comments_댓글_가지고있음(self):
        post = Post.objects.prefetch_related('comments').get(id=self.post.id) ##미리 로드하여 쿼리수 줄임
        self.assertEqual(post.comments.count(), 3)
