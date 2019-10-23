from django.shortcuts import render
# Create your views here.

def main_page(request):
  if request.method == 'GET':
    return render(request, 'main_page.html')
  return '400 Bad Request' #raise Http400
