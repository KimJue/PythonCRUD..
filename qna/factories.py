import factory
from factory.django import DjangoModelFactory
from qna.models import QnA
from userprofile.factories import UserProfileFactory


class QnAFactory(DjangoModelFactory):
    class Meta:
        model = QnA

    user = factory.SubFactory(UserProfileFactory)
    question = factory.Faker('sentence')
    answer = factory.Faker('paragraph')