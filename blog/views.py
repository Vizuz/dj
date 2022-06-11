from django.shortcuts import render
from django.http import HttpResponse

menu= ["О сайте",
       "Контакты",
       "Добавить статью",
       "Войти",]

def index(request) :
    return render(request, "blog/index.html", {"title":"Главная страница", "menu": menu})

def about(request) :
    return render(request, "blog/about.html", {"title":"О нас","menu": menu})