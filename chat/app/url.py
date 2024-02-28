from django.urls import path
from django.contrib import redirects
from .views import *
urlpatterns = [
path('',loadIndex,name="index"),
path('chat',loadChatPage,name="chat"),
path('login',loginPage,name="login"),
path('logout',logout,name="logout"),
path('<str:type>',chatType,name="chatType"),
path('message/send',submitMessage,name="sendMessage")
]