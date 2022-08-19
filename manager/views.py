from re import L
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group,Permission

from .models import Manager

# Create your views here.
def manager_list(request):
    perm=0
    for i in request.user.groups.all():
        if i.name=="masteruser":
            perm=1
    if perm==0:
         error="Access denied"
         return render(request,"back/error.html",{'error':error})

    manager=Manager.objects.all()


    
    return render(request,'back/manager.html',{'manager':manager})
def manager_del(request,pk):
    perm=0
    for i in request.user.groups.all():
        if i.name=="masteruser":
            perm=1
    if perm==0:
         error="Access denied"
         return render(request,"back/error.html",{'error':error})
    manager=Manager.objects.get(pk=pk)
    b=User.objects.filter(username=manager.utxt)
    b.delete()
    manager.delete()


    return redirect('list')    
