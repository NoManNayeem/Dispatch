from django.urls import path
from . import views

urlpatterns = [
    path('audio/<str:room_name>/', views.audio_call, name='audio_call'),
]
