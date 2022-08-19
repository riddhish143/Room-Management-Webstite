from django.db import models
from django.conf import settings
# Create your models here.
class Reservation(models.Model):
    ca=(('Teacher','Teacher'),('student','student'),('other','other'))
    Categories1=(('A-BLOCK','A-BLOCK'),('B-BLOCK','B-BLOCK'),('C-BLOCK','C-BLOCK'),('D-BLOCK','D-BLOCK'))
    stat=(('booked','booked'),('notbooked','notbooked'))
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    endtime=models.DateTimeField()
    block=models.CharField(max_length=10,choices=Categories1,default='A-BLOCK')
    number=models.IntegerField(default=40)


    purpose=models.TextField()

    Desgination=models.CharField(max_length=20,choices=ca)
    bookedby=models.CharField(max_length=20,default="-")
    status=models.CharField(max_length=20,choices=stat,default="notbooked")
    
    
    def __str__(self):
        return f"{self.user} has requested for room  from time  to "

class Rooms(models.Model):
    Categories1=(('A-BLOCK','A-BLOCK'),('B-BLOCK','B-BLOCK'),('C-BLOCK','C-BLOCK'),('D-BLOCK','D-BLOCK'))
    Categories3=(('Available','Available'),('Unavailable','Unavailable'))
    Categories2=(('class','classroom'),('meet','meetingroom'),('audit','auditorium'))
    Block=models.CharField(max_length=10,choices=Categories1)
    Type=models.CharField(max_length=20,choices=Categories2)
    Roomno=models.IntegerField()
    capacity=models.IntegerField(default="40")
    Availability=models.CharField(max_length=20,choices=Categories3)
    whenavail=models.CharField(max_length=25,default="it is available")
    def __str__(self):
        return f"In {self.Block} room of type {self.Type} with roomno {self.Roomno} is {self.Availability} with capacity of {self.capacity}"        




