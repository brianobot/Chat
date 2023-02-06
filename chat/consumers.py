import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from user.models import User
from .models import ChatRoom, Message


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the websocket connection
        print("Accepting Connection....")
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
			self.room_id,
			self.channel_name
		)
        # Close the websocket connection
        await self.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        # Deserialize the JSON data
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        content = text_data_json['content']
        sender_id = text_data_json['sender_id']

        # Save Chat to the Database
        chat_message = await database_sync_to_async(
            self.saveMessage)(content, sender_id, self.room_id)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': chat_message,
            }
        )

        # Add a field for the read status and update it based on the received message
        # You can use Django models to interact with the database

    def saveMessage(self, content, sender_id, room_id):
        sender = User.objects.get(id=sender_id)
        chat_room = ChatRoom.objects.get(room_id=room_id)
        message_obj = Message.objects.create(
            chatroom=chat_room, 
            sender=sender,
            content=content,
        )
        return {
            'action': 'message',
            'sender': str(sender),
            'content': content,
            'room_id': room_id,
            'is_read': str(message_obj.is_read),
            'created': str(message_obj.created)
        }


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))




