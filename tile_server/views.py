from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world!")


def showindex(request):
    return render(request,'index.html')