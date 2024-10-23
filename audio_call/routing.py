from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/audio/<str:room_name>/', consumers.AudioCallConsumer.as_asgi()),
]
