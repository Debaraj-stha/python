from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField( max_length=254)
    address=models.CharField(max_length=20)
    
class multipleImageUpload(models.Model):
    images=models.ImageField(upload_to='multiple_images/',null=True,default=[],max_length=255)
    userId=models.ForeignKey(User,on_delete=models.CASCADE,null=True)