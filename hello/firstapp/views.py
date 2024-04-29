from django.shortcuts import render
def index(request):
    return render(request, "index.html")

# from django.http import HttpResponse, \
#     HttpResponseRedirect, \
#     HttpResponsePermanentRedirect, \
#     HttpResponseBadRequest, \
#     HttpResponseForbidden


# def index(requsets):
#     return HttpResponse("<h2>Главная</h2>")

# def about(requsets):
#     return HttpResponse("<h2>О сайте</h2>")
#
# def contact(requsets):
#     return HttpResponseRedirect("/about")
#     # return HttpResponse("<h2>Контакты</h2>")
#
# def products(requset, productid=1):
#     category = requset.GET.get("cat", "Не задана")
#     output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
#     return HttpResponse(output)
#
# def users(request):
#     id = request.GET.get("id", "Не задано")
#     name = request.GET.get("name", "Не задано")
#     output = "<h2>Пользователь</h2>" \
#              "<h3>id:{0} Имя:{1}</h3>".format(id, name)
#     return HttpResponse(output)
# def details(request):
#     return HttpResponsePermanentRedirect("/")
#
# def access(request, age):
#     #Если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
#     if age not in range(1, 111):
#         return  HttpResponseBadRequest("Некорректные данные")
#     if age > 17: #Если возраст больше 17, то доступ разрешен
#         return HttpResponse("Доступ разрешен")
#     else: #Если нет, то возравщаем ошибку
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


