from django.urls import path

from .consumers import StatusConsumer

websocket_urlpatterns = [
    path(r'ws/status/', StatusConsumer),
]
