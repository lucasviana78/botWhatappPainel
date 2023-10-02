from django.contrib import admin
from django.urls import path

from apiBot import views

urlpatterns = [
    path('api/send', views.sendMessage, name='send'),
    path('api/recep', views.recepMessage, name='recep'),
    path('api/confirm', views.confirmMessage, name='confirm'),
]