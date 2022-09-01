"""
Views for chat app.
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Conversation, Message
from .forms import NewChatForm
from django.utils.translation import gettext as _


class ChatView(TemplateView):
    """Chat conversation starting page."""
    template_name = "chat.html"

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        room_name = self.kwargs['room_name']
        conversation, created = Conversation.objects.get_or_create(
            name=room_name
        )
        conversation_messages = Message.objects.filter(
            conversation=conversation
        ).order_by('timestamp')
        context['room_name'] = room_name
        context['conversation'] = conversation
        context['conversation_messages'] = conversation_messages
        return context


class ChatListView(TemplateView):
    """List of all created conversations."""
    template_name = "list.html"

    def get_context_data(self, **kwargs):
        context = super(ChatListView, self).get_context_data(**kwargs)
        conversations = Conversation.objects.all()
        context['conversations'] = conversations
        return context


def newChat(request):
    """Creates the new chat."""
    if request.method != 'POST':
        return HttpResponse(status=405)

    form = NewChatForm(request.POST)
    if not form.is_valid():
        messages.error(request, _('Chat name is required'))
        return HttpResponseRedirect(reverse('chat:chat_list'))

    room_name = request.POST['room_name']
    messages.success(request, _('Chat successfully created'))
    return HttpResponseRedirect(
        reverse('chat:chat_get', kwargs={'room_name': room_name})
    )


def deleteChat(request, room_name):
    """Deletes the chat."""
    if request.method != 'POST':
        return HttpResponse(status=405)

    Conversation.objects.filter(name=room_name).delete()
    messages.success(request, _('Chat successfully deleted'))
    return HttpResponseRedirect(reverse('chat:chat_list'))
