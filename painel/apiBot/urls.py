from django.contrib import admin
from django.urls import path

from apiBot import views

urlpatterns = [
    path('', views.sendMessage),
]