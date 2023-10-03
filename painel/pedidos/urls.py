from django.urls import path
from . import views

urlpatterns = [
    path('painelCozinha/', views.painelCozinha, name='painelCozinha'),
]