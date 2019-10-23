from django.shortcuts import render
from django.http import JsonResponse 
# Create your views here.

userContacts = {'user1': 'user2'}

user = {'users': userContacts}

def user_profile(request):
  if request.method == 'GET':
    return JsonResponse(user)
  return '400 Bad Request'

def user_contacts(request):
  if request.method == 'GET':
    return JsonResponse(userContacts)
  return '400 Bad Request'
