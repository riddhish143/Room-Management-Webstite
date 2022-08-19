from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
import secrets
import string
import smtplib as s
from email.message import EmailMessage as e
from django.contrib.auth.models import User
from manager.models import Manager

# Create your views here.
def changing(request):
    
    if request.method=="POST":
        email1=request.POST.get('email')
        print(email1)
        email=e()
        
        email['from']='Room booking iiitdwd'
        email['to']=email1
        email['subject']='uuuu!!!!!'
        email.set_content("12")
        with s.SMTP(host ='smtp.gmail.com',port=587) as smtp:
                 smtp.ehlo()
                 smtp.starttls()
                 smtp.login('shindesamarth19latur1234@gmail.com','pwwizkyafogdkmps')
                 smtp.send_message(email)
 


  

    return render(request,'back/changing.html')


