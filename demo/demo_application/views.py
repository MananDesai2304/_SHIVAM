from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("C2S testing server Page!")

def register(request):
  if request.method == 'POST': #TO handle Request Cmin from register.html
        username = request.POST['username']
        email = request.POST['email']
    #json().dumps
  
  return HttpResponse(json.dumps  ({   'username':username ,'email':email  }) )