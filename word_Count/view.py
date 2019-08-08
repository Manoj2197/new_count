from django.http import HttpResponse
from django.shortcuts import render

def greet(request):
    return HttpResponse("Hi,Have a good day")

def hello(request):
    return render(request,'hello.html')