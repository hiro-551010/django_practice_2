from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config import settings
import os 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', include('characters.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)