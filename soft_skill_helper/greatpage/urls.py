from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'), #127.0.0.1.8000/
    path('about/', views.about, name='about'),
    path('info/<int:info_id>/', views.info, name='info_id'), #Странички только числам
    path('info/<slug:info_slug>/', views.info_by_slug, name='info_slug'), #Страничики по любым значениям (смотреть инфу на сайте джанго)
]