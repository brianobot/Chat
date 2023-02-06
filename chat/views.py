from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from .models import ChatRoom, Message 
from .serializers import ChatRoomSerializer, MessageSerializer

# Added Support for Normal Function Views for each API view
def chat_list(request):
    return render(request, 'chat/chat_list.html')


class ChatRoomListAPI(APIView):
    def get(self, request):
        # Only get chatrooms where the current login user is part of
        chat_rooms = ChatRoom.objects.filter(member=request.user)
        data = ChatRoomSerializer(chat_rooms, many=True, context={'request': request}).data
        return Response(data)

    # For creating new chatroom
    def post(self, request):
        serializer = ChatRoomSerializer(
            data=request.data, context={"request": request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


def chat_room(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, room_id=chat_room_id)
    messages = chat_room.messages.all()
    return render(request, 'chat/chat_room.html', {'room_id': chat_room_id, 'messages': messages})


class ChatRoomAPI(APIView):
    # TODO: Introduce Pagination to limit the number of messages returned
    def get(self, request, chat_room_id):
        chat_room = get_object_or_404(ChatRoom, room_id=chat_room_id)
        messages = chat_room.messages.all().order_by('-created')
        data = MessageSerializer(messages, many=True, context={'request':request}).data
        return Response(data)


# Version 2
# class MessagesView(ListAPIView):
# 	serializer_class = ChatMessageSerializer
# 	pagination_class = LimitOffsetPagination

# 	def get_queryset(self):
# 		room_id = self.kwargs['room_id']
# 		return ChatMessage.objects.filter(messages__room_id=room_id).order_by('-created')