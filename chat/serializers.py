from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Message, ChatRoom


class ChatRoomSerializer(serializers.ModelSerializer):
    member = UserSerializer(many=True, read_only=True)
    members = serializers.ListField(write_only=True)

    def create(self, validatedData):
        memberObject = validatedData.pop("members")
        chatRoom = ChatRoom.objects.create(*validatedData)
        chatRoom.memeber.set(memberObject)
        return chatRoom

    class Meta:
        model = ChatRoom
        exclude = ("id",)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ("id", "chatroom")
