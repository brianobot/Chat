from rest_framework import generics, permissions
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ChatRoom, Message 
from .serializers import ChatRoomSerializer, MessageSerializer


# Added Support for Normal Function Views for each API view
@permission_classes(IsAuthenticated)
def chat_list(request):
    return render(request, 'chat/chat_list.html')


class ChatRoomListAPI(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = (authentication.BasicAuthentication, authentication.SessionAuthentication, authentication.TokenAuthentication)

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


@permission_classes(IsAuthenticated)
def chat_room(request, chat_room_id):
    chat_room = get_object_or_404(ChatRoom, room_id=chat_room_id)
    messages = chat_room.messages.all()
    return render(request, 'chat/chat_room.html', {'room_id': chat_room_id, 'messages': messages})


class ChatRoomAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # TODO: Introduce Pagination to limit the number of messages returned
    def get(self, request, chat_room_id):
        chat_room = get_object_or_404(ChatRoom, room_id=chat_room_id)
        messages = chat_room.messages.all().order_by('-created')
        data = MessageSerializer(messages, many=True, context={'request':request}).data
        return Response(data)


@api_view(['PATCH'])
def update_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.is_read = True
    message.save()
    return Response({'message': 'Message updated successfully.'}, status=status.HTTP_200_OK)


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]



# Version 2
# class MessagesView(ListAPIView):
# 	serializer_class = ChatMessageSerializer
# 	pagination_class = LimitOffsetPagination

# 	def get_queryset(self):
# 		room_id = self.kwargs['room_id']
# 		return ChatMessage.objects.filter(messages__room_id=room_id).order_by('-created')