import factory
from factory.django import DjangoModelFactory
from userprofile.models import UserProfile


class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    user_id = factory.Sequence(lambda n: f'user_{n}')
    password = factory.Faker('password')
    email = factory.Sequence(lambda n: f'user{n}@example.com')