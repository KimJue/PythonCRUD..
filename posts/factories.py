import factory
from django.contrib.auth.models import User
from .models import Post, Comment

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    content = factory.Faker('text')
    author = factory.SubFactory(UserFactory)

class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker('text')
    post = factory.SubFactory(PostFactory)
