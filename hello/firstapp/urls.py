from django.urls import path
from django.views.generic import TemplateView

from .import views

urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name="first_app/about.html")),
    path('contact/', TemplateView.as_view(template_name="first_app/contact.html",
                                          extra_context={"work": "Поменял значение work"})),
]