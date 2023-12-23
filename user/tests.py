from django.test import TestCase

from user.factories import UserFactory


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()

    def test_user_is_created(self):
        self.assertTrue(self.user)

    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)
