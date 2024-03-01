from django.urls import path
from django.contrib import redirects
from .views import *
urlpatterns = [
path('',loadIndex,name="index"),
path('chat',loadChatPage,name="chat"),
path('login',loginPage,name="login"),
path('logout',logout,name="logout"),
path('<str:type>',chatType,name="chatType"),
path('message/send',submitMessage,name="sendMessage"),
path('chat/group',loadGroups,name='groups'),
path('group/add',createGroup,name="groupAdd"),
path('chat/individual',individualChat,name="individual-chat"),
]