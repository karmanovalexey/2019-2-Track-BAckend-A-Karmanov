from django.shortcuts import render
from django.http import JsonResponse 
# Create your views here.

chat1 = {'user1': 'chat'}

chats = {'chats': chat1}

def chat_list(request):
  if request.method == 'GET':
    return JsonResponse(chats)
  return '400 Bad Request'

def chat_content(request):
  if request.method == 'GET':
    return JsonResponse(chat1)
  return '400 Bad Request'