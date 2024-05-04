import datetime
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return render(request, "first_app/index.html")

def about(request):
    return render(request, "first_app/about.html")

def contact(request):
    return render(request, "first_app/contact.html")