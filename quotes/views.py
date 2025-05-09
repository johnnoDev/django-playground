from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hola mundo desde Django!")


def monday(request):
    return HttpResponse("Hola Lunes")


def tuesday(request):
    return HttpResponse("Hola Martes")
