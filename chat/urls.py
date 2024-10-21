# chat/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
    path('chat/<int:chat_id>/send/', views.send_message, name='send_message'),
    path('chats/', views.chat_list, name='chat_list'),
]
