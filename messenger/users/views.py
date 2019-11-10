from django.shortcuts import render
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import User

userContacts = {'user1': 'user2'}

placeholder = {'users': userContacts}

def user_profile(request):
    if request.method == 'GET':
        return JsonResponse(placeholder)
    return HttpResponseNotAllowed(['GET'])

def get_user(nickname):
    try:
        user = User.objects.filter(username=nickname)
    except ObjectDoesNotExist:
        user = None
    except MultipleObjectsReturned:
        user = User.objects.filter(username=nickname).first
    return user

def user_contacts(request):
  if request.method == 'GET':
    return JsonResponse(userContacts)
  return HttpResponseNotAllowed(['GET'])
