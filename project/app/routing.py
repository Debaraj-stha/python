from django.urls import path
from . import consumers

wobsocket_urlpatterns = [
    path("ws/wc/", consumers.MyConsumer.as_asgi()),
]
