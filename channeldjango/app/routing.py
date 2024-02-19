from django.urls import path
from myapp import consumers

websocket_urlPatterns = [path("ws/wc/", consumers.MyConsumer.as_asgi())]
