import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model  = User

    username = factory.Sequence(lambda n: f"test_user_{n}")
    email = factory.Sequence(lambda n: f"test_user_{n}@example.com")
    password = 'testpassword12secure'