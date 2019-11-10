from django.shortcuts import render
from django.http import HttpResponseNotAllowed 
# Create your views here.

def main_page(request):
  if request.method == 'GET':
    return render(request, 'main_page.html')
  return HttpResponseNotAllowed(['GET'])
