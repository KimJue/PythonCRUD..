import factory
from django.contrib.auth.models import User
from .models import Alert


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class AlertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Alert

    title = factory.Faker('sentence')
    message = factory.Faker('text')
    is_active = True
    user = factory.SubFactory(UserFactory)
