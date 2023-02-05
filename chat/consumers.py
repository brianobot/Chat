from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the websocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Close the websocket connection
        await self.close()

    async def receive(self, text_data):
        # Deserialize the JSON data
        text_data_json = json.loads(text_data)
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        content = text_data_json['content']

        # Store the message in the database
        # Add a field for the read status and update it based on the received message
        # You can use Django models to interact with the database

        # Send the message to the receiver
        await self.send(text_data=json.dumps({
            'sender': sender,
            'content': content,
        }))

        # send a read receipt to the sender
        await self.send(text_data=json.dumps({
            'receiver': receiver,
            'is_read': True,
        }))