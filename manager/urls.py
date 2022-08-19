from . import views
from django.urls import re_path



urlpatterns = [
    re_path(r'^adm/manager/list/$',views.manager_list,name='list'),
    re_path(r'^adm/manager/del/(?P<pk>\d+)/$',views.manager_del,name='managerdeleting'),
    
]