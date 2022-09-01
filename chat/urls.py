"""
Urls for chat app.
"""
from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path('get/<str:room_name>/', views.ChatView.as_view(), name='chat_get'),
    path('list/', views.ChatListView.as_view(), name='chat_list'),
    path('new/', views.newChat, name='chat_new'),
    path('delete/<str:room_name>/', views.deleteChat, name='chat_delete'),
]
