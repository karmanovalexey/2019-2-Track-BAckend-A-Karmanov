from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed 
from .models import Chat
from users.models import Member, User
# Create your views here.

chat1 = {'user1': 'chat'}

chats = {'chats': chat1}

def chat_list(request):
    if request.method == 'GET':
        return JsonResponse(chats)
    return HttpResponseNotAllowed(['GET'])

def get_chat_list():
    chat_list = Chat.objects.all()
    return list(chat_list)

def create_user_chat(user):
    chat = Chat.objects.create()
    Member.objects.create(chat_id=chat.chat_id, user_id=user.user_id)
    return chat

def chat_content(request):
    if request.method == 'GET':
       return JsonResponse(chat1)
    return HttpResponseNotAllowed(['GET'])