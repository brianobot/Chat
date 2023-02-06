from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path('chats/', views.chat_list, name='chats-list'),
    path('api/chats/', views.ChatRoomListAPI.as_view(), name='api-chats-list'),

    path('chat/<str:chat_room_id>/', views.chat_room, name='chat-room'),
    path('api/chat/<str:chat_room_id>/', views.ChatRoomAPI.as_view(), name='api-chat-room'),

    # API endpoint to update read receipt of message
    path('messages/<int:message_id>/update/', views.update_message, name='update_message'),

    path('api-token-auth/', obtain_auth_token),
]