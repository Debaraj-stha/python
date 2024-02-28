from django.urls import path
from .consummers import MyConummer
websocketurlpatterns=[
    path("ws/wc", MyConummer.as_asgi())
]