from django.urls import path
from . import views

urlpatterns = [
    path('painelPedidos/', views.painelPedidos, name='painelPedidos'),
    path('painelCozinha/', views.painelCozinha, name='painelCozinha'),
]