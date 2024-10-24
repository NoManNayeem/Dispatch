from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),                # Admin route
    path('', include('accounts.urls')),             # Routes for accounts (landing, login, register)
    path('chat/', include('chat.urls')),            # Routes for chat functionality
    
    
    path('video_call/', include('video_call.urls')),
    path('audio_call/', include('audio_call.urls')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
