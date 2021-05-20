from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
import os 
from . import views

app_name = 'characters'

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('signup/', views.signup, name='signup'),
    path('list/', views.CharaList.as_view(), name='list'),
    path('chara/', views.chara, name='chara'),
    path('table/', views.CharaTable.as_view(), name='table'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)