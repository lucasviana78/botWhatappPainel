from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sendMessage(request):
    return HttpResponse('enviando' + "|" + " 1" + "|" + " 11953635910 " + "|" + " Pato não voa")


def recepMessage(request):
    return HttpResponse("")


def confirmMessage(request):
    return HttpResponse("")