import factory
from .models import QnA

class QnAFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = QnA

    question = factory.Faker('sentence')
    answer = factory.Faker('text')
