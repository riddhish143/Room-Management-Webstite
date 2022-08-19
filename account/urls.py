from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import re_path



urlpatterns = [
    re_path(r'^change/$',views.changing,name="changing"),
    
    

    
    
]