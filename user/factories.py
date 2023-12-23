import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"test_user_{n}@example.com")
    username = factory.Sequence(lambda n: f"test_user_{n}")
    password = factory.Sequence(lambda n: "testpassword_{n}")
