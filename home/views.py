from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hey I am a Django Server")
    return  render(request , "login.html")

def success_page(request):
    return HttpResponse("Hey I am a success page ")
