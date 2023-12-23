import factory

from user.factories import UserFactory
from .models import ChatRoom, Message


class ChatRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatRoom

    room_id = factory.Sequence(lambda n: f"room_{n}")


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    sender = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)
    content = "test message content"
    chatroom = factory.SubFactory(ChatRoomFactory)
