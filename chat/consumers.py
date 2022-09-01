"""
Consumers for chat app.
"""
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Conversation, Message


class PublicChatConsumer(WebsocketConsumer):
    """Public chat consumer class."""
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.conversation_name = None
        self.conversation = None

    def connect(self):
        """Handles websocket connection."""
        self.accept()
        self.conversation_name = f"""{self.scope['url_route']
                                ['kwargs']['conversation_name']}"""
        self.conversation, created = Conversation.objects.get_or_create(
            name=self.conversation_name
        )
        if self.scope["user"].is_authenticated:
            self.conversation.join(self.scope["user"])
        async_to_sync(self.channel_layer.group_add)(
            self.conversation_name,
            self.channel_name
        )

    def disconnect(self, code):
        """Handles websocket disconnection."""
        if self.scope["user"].is_authenticated:
            self.conversation.leave(self.scope["user"])
        print("Disconnected!")
        return super().disconnect(code)

    def receive(self, text_data):
        """Handles messages from client side."""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope["user"]
        Message.objects.create(
            conversation=self.conversation,
            user=username if username.is_authenticated else None,
            content=message
        )

        async_to_sync(self.channel_layer.group_send)(
            self.conversation_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': str(username)
            }
        )

    def chat_message(self, event):
        """Sends message to the room."""
        message = event['message']
        username = event['username']
        self.send(text_data=json.dumps({
            'type': 'message',
            'message': username + ': ' + message
        }))
