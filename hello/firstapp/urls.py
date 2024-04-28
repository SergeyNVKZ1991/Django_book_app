from django.urls import path
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^about', views.about, name='about'),
    re_path(r'^contact', views.contact, name='contact'),
    path('products/', views.products), #маршрукт по умолчанию
    path('products/<int:productid>/', views.products),
    path('users/', views.users), #маршрукт по умолчанию
    path('users/<int:id>/<name>', views.users),
    path('', views.index, name='index'),
]