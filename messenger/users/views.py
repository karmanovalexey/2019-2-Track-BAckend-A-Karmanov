from django.shortcuts import render
from django.http import JsonResponse 
# Create your views here.

userContacts = {'placeholder': 'placeholder'}

user = {'placeholder': user_contacts}

def user_profile(request):
  if request.method == 'GET':
    return JsonResponse(user)
  return '400 Bad Request'

def user_contacts(request):
  if request.method == 'GET':
    return JsonResponse(user_contacts)
  return '400 Bad Request'
