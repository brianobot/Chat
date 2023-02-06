from django.test import TestCase

from user.models import User
from user.factories import UserFactory
from .models import ChatRoom, Message


class ChatTestCase(TestCase):
    def setUp(self):
        self.user1 = UserFactory.create()
        self.user2 = UserFactory.create()
        self.chatroom = ChatRoom.objects.create(room_id='tets-room')
        self.chatroom.member.add(self.user1)
        self.chatroom.member.add(self.user2)
        self.chatroom.save()
        self.message = Message.objects.create(
            sender=self.user1,
            content='Hello, this is a test message',
            chatroom=self.chatroom
        )
    
    def test_create_message(self):
        message = Message.objects.create(
            sender=self.user1,
            content='Hello, this is another test message',
            chatroom=self.chatroom
        )
        self.assertEqual(Message.objects.count(), 2)
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.content, 'Hello, this is another test message')
        self.assertEqual(message.chatroom, self.chatroom)

    def test_update_message(self):
        self.message.is_read = True
        self.message.save()
        self.assertTrue(Message.objects.get(id=self.message.id).is_read)

    def test_delete_message(self):
        self.message.delete()
        self.assertEqual(Message.objects.count(), 0)

    def test_create_chatroom(self):
        chatroom = ChatRoom.objects.create(room_id='Test Chat Room 2')
        self.assertEqual(ChatRoom.objects.count(), 2)
        self.assertTrue(chatroom.room_id ==  'Test Chat Room 2')
        
    def test_delete_chatroom(self):
        self.chatroom.delete()
        self.assertEqual(ChatRoom.objects.count(), 0)