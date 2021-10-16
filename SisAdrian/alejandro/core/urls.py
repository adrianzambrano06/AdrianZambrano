from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('inicio', views.inicio,name='inicio'),
    path('', views.paginalogin, name='paginalogin'),
    path('reg', views.registroUsuario, name='reg'),
]