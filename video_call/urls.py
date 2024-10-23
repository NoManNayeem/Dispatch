from django.urls import path
from . import views

urlpatterns = [
    path('video/<str:room_name>/', views.video_call, name='video_call'),
]
