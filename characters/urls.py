from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'characters'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('list/', views.list, name='list'),
]