from django.urls import path

from . import views


urlpatterns = [
    path('chats/', views.chat_list, name='chats-list'),
    path('api/chats/', views.ChatRoomListAPI.as_view(), name='api-chats-list'),

    path('chat/<str:chat_room_id>/', views.chat_room, name='chat-room'),
    path('api/chat/<str:chat_room_id>/', views.ChatRoomAPI.as_view(), name='api-chat-room'),
]