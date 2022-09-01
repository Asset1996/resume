"""
Models page for chat app.
"""
import uuid
from main.models import User
from django.db import models


class Conversation(models.Model):
    """Model for conversations."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f"{self.name} ({self.get_online_count()})"


class Message(models.Model):
    """Model for messages."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    user = models.ForeignKey(
        User, default=None, blank=True, null=True,
        on_delete=models.CASCADE, related_name="messages_from_me"
    )
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return f"User {self.user.email}: {self.content} [{self.timestamp}]"
        return f"Anonymous user: {self.content} [{self.timestamp}]"
