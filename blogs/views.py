from django.shortcuts import render, HttpResponse





def index(request):
  return HttpResponse('Hello world ')

def home(request):
  return render(request,'blogs/index.html')


# Create your views here.
