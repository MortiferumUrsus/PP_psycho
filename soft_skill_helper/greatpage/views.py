from django.http import HttpResponse
from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("<h1>Главная страничка готова</h1>")

def info(request):
    return HttpResponse("<h1>Страничка с инфой готова</h1>")