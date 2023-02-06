import factory

from user.factories import UserFactory
from .models import ChatRoom, Message


class ChatRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChatRoom

    # member = 


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    sender = factory.SubFactory(UserFactory)
    receiver = factory.SubFactory(UserFactory)
    content = "test content"
    chatroom = factory.SubFactory(ChatRoomFactory)