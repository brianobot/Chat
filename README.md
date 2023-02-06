# Real-Time Peer-To-Peer Messaging API

## Description

## Features
- Real Time peer-to-peer messaging
- Implemented over an api (and called using an api key/token)
- Read Receipts should show in api response
- Updating read status is done over another api. The frontend would make the api callonce the message is read

## Setup And Usage


 - ### API Endpoints:
   - /api/users/  : List all the user currently registered on the system
   - /api/signup/ : Endpoint for Creating a user instance in the system
   - /api/login/  : Endpoint for Authenicating a user into the system, returns auth token
   - /api/chats/  : Returns All Chatroom that involves the current auth user
   - /api/chat/<str:room_id>/ : Returns a list of chats connected to the specified ChatRoom
     - Websocket connection is expected from the frontend at this endpoint

## Implementation:
All chat-message instances are part of a chat-room instance which contains at least two users.

A user can see all chat-room that he is involved in by going the chat endpoint (authorization)
    View URL - `/chat/`
A user can go into and interact with a chat-room by going to the chat-room endpoint (identification and authorization)
    View URL - `/chat/<chat-room-id>/`
    Once in the chat-room view, a websocket is created for real-time connection with the server and hence the other connected user
    Websocket url - `/chat/<chat-room-id>/`

