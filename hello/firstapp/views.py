from django.shortcuts import render
from django.http import HttpResponse

def index(requsets):
    return HttpResponse("<h2>Главная</h2>")

def about(requsets):
    return HttpResponse("<h2>О сайте</h2>")

def contact(requsets):
    return HttpResponse("<h2>Контакты</h2>")

def products(requsets, productid=1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(requsets, id=1, name="Максим"):
    output = "<h2>Пользователь</h2>" \
             "<h3>id:{0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)




