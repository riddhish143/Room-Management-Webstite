import codeop
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout

from .models import cont
import datetime

# Create your views here.
def messaging(request):
    if not request.user.is_authenticated:
        return redirect('using')
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1 :
        day = "0" + str(day)
    if len(str(month)) == 1 :
        month = "0" + str(month)

   
    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        if name=="" or email=="" or message=="":
            message="please input all fields"
            return render(request,'front/messaging.html',{'messaging':message})
        yourmessage=cont(name=name,email=email,message=message,date=today,time=time)
        yourmessage.save()  
        message="your message has been succesully sent."
        return render(request,'front/messaging.html',{'messaging':message})


    
    return render(request,'front/contact.html')


def contactinfo(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    msg=cont.objects.all()

    return render(request,'back/contactinfo.html',{'msg':msg})

def contact_del(request,pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    b=cont.objects.filter(pk=pk)
    b.delete()
    return redirect('contactinfo')

