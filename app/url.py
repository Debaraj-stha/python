from django.urls import path, include

from app.views import *

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("find_user_view", find_user_view, name="find_user_view"),
]
