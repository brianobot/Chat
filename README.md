# Django Real-Time Chat API

## Description
A high-performance, secure, and scalable real-time chat API built with Django. This API allows developers to easily build chat applications that can handle large amounts of messages and users.

## Key Features (Completed)
- ✔ Real-time chat communication using WebSockets
- ✔ User authentication and authorization using token-based authentication
- ✔ Scalable architecture to handle large numbers of users and messages
- ✔ Efficient database design to store and retrieve messages in real-time
- ✔ Efficient database design to store and retrieve messages in real-time
- ✔ Robust security features to protect against malicious attacks


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.x
- Pip 

### Installing
1. Clone the repository:  
```python
https://github.com/brianobot/Chat.git
```
  
2. Setup Virtual Environment:  
```python
pip install pipenv
pipenv shell
```

3. Install the required packages:  
```python
pipenv install -r requirements.txt
```

4. Run the development server:  
```python
python manage.py runserver
```


## API Endpoints:
The API has the following endpoints for authentication, messages, and chat rooms:
   - `/api/v1/api-token-auth/`:  Endpoint for obtaining tokens
   - `/api/v1/signup/` : Endpoint for Creating a user instance in the system
   - `/api/v1/login/`  : Endpoint for Authenicating a user, returns auth token
   - `/api/v1/users/`  : List all the user currently registered on the system
   - `/api/v1/chats/`  : Lists All Chatroom that involves the current auth user
   - `/api/v1/chat/<str:room_id>/` : Returns a list of chats connected to the specified ChatRoom
     - Websocket connection is expected from the frontend at this endpoint for real time peer to peer messaging
   - `api/v1/messages/<int:message_id>/update/` : EndPoint for updating the read receipt of a message (specified by the message_id)


## Object Concepts:
All chat-message instances are part of a chat-room instance which contains at least two users.

A user can see all chat-room that he is involved in by going the chat endpoint.   
    View URL - `api/v1/chat/`  
A user can go into and interact with a chat-room by going to the chat-room endpoint
    View URL - `api/v1/chat/<chat-room-id>/`

Once in the chat-room view, a websocket is created for real-time connection with the server and hence the other connected user.    
  Websocket url - `ws/chat/<chat-room-id>/`


## Maintainer:
- Brian Obot <brianobot9@gmail.com>
