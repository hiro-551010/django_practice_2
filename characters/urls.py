from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from config import settings
import os 
app_name = 'characters'

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('signup/', views.signup, name='signup'),
    path('list/', views.CharaList.as_view(), name='list'),
    path('chara/', views.chara, name='chara'),
    path('table/', views.CharaTable.as_view(), name='table'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)