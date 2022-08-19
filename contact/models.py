from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.

class cont(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    message=models.TextField()
    date=models.CharField(max_length=20,default="-")
    time=models.CharField(max_length=20,default="-")

    def __str__(self):
        return self.name
