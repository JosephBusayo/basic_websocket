#similar to urls.py but for websocket

from django.urls import path

from .consumers import WSConsumer


ws_urlpatterns = [
    path('ws/home/', WSConsumer.as_asgi())
]