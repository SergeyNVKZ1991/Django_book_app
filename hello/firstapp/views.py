import datetime
from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, "first_app/home.html")

