from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='indexLogin'),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.indexSystem, name='indexSystem')
]