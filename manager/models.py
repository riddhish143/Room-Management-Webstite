from django.db import models
from django.conf import settings

# Create your models here.
class Manager(models.Model):
    name=models.CharField(max_length=30)
    utxt=models.TextField()
    email=models.TextField(default="")
    def __str__(self):
        return self.name
class accepteduser(models.Model):
    username=models.CharField(max_length=25)
    start=models.CharField(max_length=20)
    end=models.CharField(max_length=20)
    area=models.CharField(max_length=5)
    numb=models.IntegerField(default=0)

    
    

    