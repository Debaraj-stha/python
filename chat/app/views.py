from datetime import datetime
import json
from os import name
from tokenize import group
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# Create your views here.
def loadIndex(request):
    return render(request,'index.html')
def loadChatPage(request):
    groupName=request.GET.get('group')
    userId=request.GET.get('user')
    group=Group.objects.filter(groupName=groupName)
    user=User.objects.filter(id=userId)
    if group.exists():
        groupMessages=Message.objects.filter(group=group.first())
        messages=[]
        for message in groupMessages:
            messages.append({
                 "message":message.message,
                "group":message.group.groupName,
                "to":None,
                "from": message.f,
                "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
            })
    if userId is not None and user.exists():
        userMessages=Message.objects.filter(Q(to=user.first()) |Q(f=user.first()))
        messages=[]
        for message in userMessages:
            messages.append({
                 "message":message.message,
                "group":None,
                "to":message.to.name if message.to else None,
                "from": message.f.name if message.f else None,
                "isSender":userId==message.f.id,
                "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
            })
            
    return render(request,'chat.html',{'messages':messages})
def loginPage(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        user=User.objects.filter(name=name).first()
        if user is  None:
            instance=User(name=name)
            instance.save()
        
        res=redirect('/')
        res.set_cookie('name',name)
        return res
    return render(request,'login.html')
def logout(request):
    response=redirect('login')
    response.delete_cookie('name')
    return response
def chatType(request, type):
    myMessages = []
    # name = request.COOKIES.get('name')
    messages = None  # Initialize messages with a default value
    try:
        if type == 'group':
            messages = Message.objects.exclude(group__isnull=True)
            for message in messages:
                myMessages.append({
                    "message": message.message,
                    "group": message.group.groupName,
                    "to": None,
                    "from": message.f,
                    "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
                })

        else:
            messages = Message.objects.exclude(to__isnull=True).distinct('to', 'f')
            print(messages)
            for message in messages:
                myMessages.append({
                    "message": message.message,
                    "group": None,
                    "to": message.to,
                    "from": message.f,
                    "created_at": message.created_at.strftime("%y-%m-%d %H:%M:%S")
                })

        return render(request, 'users.html', {"messages": myMessages})
    except Exception as e:
        print(e)
        return render(request, 'users.html', {"messages": myMessages})

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
def loadGroups(request):

    my_groups=[]
    groups=Group.objects.all()
    print(groups)
    for group in groups:
        my_groups.append({'name':group.groupName})
    print("my_groups")
    return render(request,'groups.html',{'groups':my_groups})
def individualChat(request):
    cookie=request.COOKIES.get('name')
    users=[]
    user=User.objects.exclude(name=cookie)
    for u in user:
        users.append({'name':u.name,"id":u.id})
    return render(request,'individual.html',{'users':users})
    
    

def createGroup(request):
    data=request.POST
    name=data.get('group_name')
    g=Group(groupName=name)
    g.save()
    return redirect('groups')