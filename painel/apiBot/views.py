from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sendMessage(request):
    return HttpResponse('Enviando')