from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), #127.0.0.1.8000/
    path('info/', views.info),
]