from django.http import HttpResponse
from django.shortcuts import render

from app.consumers import MyConsumer


# Create your views here.
def index(request):
    myConsumer = MyConsumer()
    myConsumer.custom_method("Hello from view!")
    return HttpResponse("<H1> This is a test page</H1>")
