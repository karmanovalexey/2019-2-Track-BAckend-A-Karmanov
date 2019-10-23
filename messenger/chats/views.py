from django.shortcuts import render
from django.http import JsonResponse 
# Create your views here.

chat1 = {'placeholder': 'placeholder'}

chats = {'placeholder': chat1}

def chat_list(request):
  return JsonResponse(chats)
