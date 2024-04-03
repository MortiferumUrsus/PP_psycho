from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("<h1>Главная страничка готова</h1>")

def info(request, info_id):
    return HttpResponse(f"<h1>Страничка с инфой готова</h1><p>id: {info_id}</p>")

def info_by_slug(request, info_slug):
    return HttpResponse(f"<h1>Страничка с инфой готова</h1><p>slug: {info_slug}</p>")

def page_not_found(request, exception):
    return HttpResponseRedirect("/")