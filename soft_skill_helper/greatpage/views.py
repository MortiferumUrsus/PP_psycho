from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ["О сайте", "Обратная связь", "Войти", "Телеграм бот"]

def index(request): #HttpRequest
    #t = render_to_string('greatpage/index.html') #Шаблоны писать только в UTF-8!
    #return HttpResponse(t)
    data ={
        'title': 'Главная страничка',
        'menu': menu,
    }
    return render(request, 'greatpage/index.html', context=data)

def contacts(request):
    return render(request, 'greatpage/contacts.html', {'title': 'Контакты'})

def info(request, info_id):
    return HttpResponse(f"<h1>Страничка с инфой готова</h1><p>id: {info_id}</p>")

def info_by_slug(request, info_slug):
    return HttpResponse(f"<h1>Страничка с инфой готова</h1><p>slug: {info_slug}</p>")

def page_not_found(request, exception):
    return HttpResponseRedirect("/")