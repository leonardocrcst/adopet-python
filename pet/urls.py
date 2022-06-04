from django.urls import path
from .html import home

urlpatterns = [
    path('home/', home),
]