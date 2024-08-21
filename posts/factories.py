import factory

from userprofile.factories import UserProfileFactory
from .models import Post, Comment


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    user_id = factory.SubFactory(UserProfileFactory)
    title = factory.sequence(lambda n: "Post %s" % n)
    content = factory.Sequence(lambda n: "Post body %s" % n)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker('text')
    post = factory.SubFactory(PostFactory)
