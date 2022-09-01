from django.contrib import admin
from .models import Conversation, Message


class ConversationAdmin(admin.ModelAdmin):
    """Custom Conversation models ConversationAdmin class."""
    ordering = ["id"]
    list_display = ["name", "timestamp"]
    search_fields = ["name"]
    empty_value_display = "--empty--"


class MessageAdmin(admin.ModelAdmin):
    """Custom Message models MessageAdmin class."""
    ordering = ["id"]
    list_display = ["conversation", "user", "content"]
    search_fields = ["content"]
    empty_value_display = "--empty--"


admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message, MessageAdmin)
