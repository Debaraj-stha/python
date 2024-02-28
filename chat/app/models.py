
import json
from django.db import models

from  django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ValidationError
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
class Group(models.Model):
    groupName=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.groupName
class Message(models.Model):
    message=models.TextField()
    to=models.ForeignKey(User, related_name='to',on_delete=models.CASCADE,null=True,blank=True)
    f=models.ForeignKey(User,related_name="f",on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    group=models.ForeignKey(Group,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return (self.message )
    def clean(self):
        if self.to==self.f:
            raise ValidationError({"to": "You can't send message to yourself"})
@receiver(post_save, sender=Message)
def sendMessage(sender,instance,created,**kwargs):
    if created:
        channel_layer=get_channel_layer()
        response={
            "message":instance.message,
            "to":instance.to.name if instance.to else None,
            "from":instance.f.name if instance.f else None,
            "created_at": instance.created_at.strftime("%y-%m-%d %H:%M:%S"),
            "group":instance.group.groupName if instance.group else None
        }
        async_to_sync(channel_layer.group_send)(
            "group_%"%(instance.group.name if instance.group is not None else instance.to.id),
            {"type": "chat.message", "text": json.dumps(response)},
        )
        print("message is send ")
        
        
class GroupMemders(models.Model):
    memder=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    
    

