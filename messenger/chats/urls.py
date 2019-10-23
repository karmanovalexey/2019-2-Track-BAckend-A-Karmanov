from chats.views import chat_list, chat_content
from django.urls import path

urlpatterns = [path('', chat_list, name='chat_list'),
                path('chat/', chat_content, name='chat_content')]
