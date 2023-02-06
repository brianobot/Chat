import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from user.models import User
from .models import ChatRoom, Message


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the websocket connection
        print("Acceptin Connection....")
        self.room_id = self.scope['url_route']['kwargs']['room_id']

        await self.accept()

    async def disconnect(self, close_code):
        # Close the websocket connection
        print("Closing Connection...")
        await self.close()

    async def receive(self, text_data):
        # Deserialize the JSON data
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        room_id = text_data_json['room_id']
        

        if action == 'message':
            content = text_data_json['content']
            sender_id = text_data_json['sender']
            receiver_id = text_data_json['receiver']
            chatMessage = await database_sync_to_async(
                self.saveMessage
            )(content, sender_id, receiver_id, room_id)
        elif action == 'typing':
            chatMessage = text_data_json

        await self.channel_layer.group_send(
            room_id,
            {
                'type': 'chat_message',
                'message': chatMessage,
            }
        )

        # Store the message in the database
        # Add a field for the read status and update it based on the received message
        # You can use Django models to interact with the database

        # Send the message to the receiver
        await self.send(text_data=json.dumps({
            'sender': sender_id,
            'content': content,
        }))

        # send a read receipt to the sender
        await self.send(text_data=json.dumps({
            'receiver': receiver_id,
            'is_read': True,
        }))

    def saveMessage(self, content, sender_id, receiver_id, room_id):
        sender = User.objects.get(id=sender_id)
        receiver = User.objects.get(id=receiver_id)
        chat_room = ChatRoom.objects.get(room_id=room_id)
        message_obj = Message.objects.create(
            chatroom=chat_room, 
            sender=sender,
            receiver=receiver, 
            content=content,
        )
        return {
            'action': 'message',
            'room_id': room_id,
            'content': content,
            'sender': sender_id,
            'receiver': receiver_id,
            'created': str(message_obj.created)
        }