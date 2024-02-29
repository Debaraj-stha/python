from datetime import datetime
import json
from os import name
from tokenize import group
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def loadIndex(request):
    return render(request,'index.html')
def loadChatPage(request):
    groupName=request.GET.get('group')
    userName=request.GET.get('user')
    print(groupName, userName)
    return render(request,'chat.html',{'groupName':groupName, 'userName':userName})
def loginPage(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        user=User.objects.filter(name=name).first()
        if user is  None:
            instance=User(name=name)
            instance.save()
        
        res=redirect('/')
        # res.set_cookie('name',name)
        return res
    return render(request,'login.html')
def logout(request):
    response=redirect('login')
    response.delete_cookie('name')
    return response
def chatType(request,type):
    myMessages=[]
    if type=='group':
        messages = Message.objects.exclude(group__isnull=True)

        for message in messages:
            myMessages.append({
                "message":message.message,
                "group":message.group.groupName,
                "to":None,
                "from": message.f,
                "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
            })
        
    else:
        messages=Message.objects.exclude(to__isnull=True)
        for message in messages:
            myMessages.append({
                "message":message.message,
                "group":None,
                "to":message.to,
                "from": message.f,
                 "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
            })
    return render(request,'users.html',{"messages":myMessages})

@csrf_exempt
def submitMessage(request):

    try:
        fro=request.COOKIES.get('name')
        user=User.objects.filter(name=fro).first()
        data=json.loads(request.body)
        print(f"data {str(data)}")
        m=data.get('message')
        to=data.get('to',None)
        group=data.get('group',None)
        toUser=None
        groupInstance=None
        if to is not None:
            toUser=User.objects.filter(id=to).first()
        # if group is not None:
        groupInstance=Group.objects.filter(groupName=group if group is not None else 'demo').first()
        message=Message(message=m,to=toUser,f=user,group=groupInstance)
      
        message.save()
        data={
            "message":message.message,
            "to":message.to.name if message.to else None,
            "from":message.f.name if message.f else None,
            "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S"),
            "group":message.group.groupName if message.group else None
            
        }
        return JsonResponse({"status":True, "message":"message send successfully"},status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"message":f"Exception occured:{e}","status":False},status=500)
    