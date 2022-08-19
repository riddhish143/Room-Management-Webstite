from . import views
from django.urls import re_path



urlpatterns = [
    re_path(r'^home/$',views.first,name='first'),
    re_path(r'^loggingout/$',views.userloggingout,name='outing'),
    re_path(r'^registering/$',views.userregistering,name='winning'),
    re_path(r'^changingpass/$',views.changingpassword,name='changingpasswording'),
    re_path(r'^forming/$',views.createdform,name='forming'),
    re_path(r'^bethechange/$',views.plussing,name='plus'),
    re_path(r'^status/$',views.roomstatus,name='status'),
    re_path(r'^$',views.userslogin,name="using"),
    re_path(r'^image/$',views.image,name="image"),
    re_path(r'^adm/$',views.panel,name="panel"),
    re_path(r'^adm/roominfo/$',views.roominfo,name="info"),
    re_path(r'^adm/room/$',views.room,name="room"),
    re_path(r'^adm/roomrequest/$',views.requestedroom,name="requested"),
    re_path(r'^adm/edit/(?P<pk>\d+)/$',views.edit,name="edit"),
    re_path(r'^adm/del/(?P<pk>\d+)/$',views.deleting,name="delete"),
    re_path(r'^adlogging/$',views.mylogin,name="mylogin"),
    re_path(r'^adlogggingout/$',views.mylogout,name="mylogout"),
    re_path(r'^contact/$',views.contacting,name="contact"),
    re_path(r'^accept/(?P<pk>\d+)/$',views.accept,name='accept'),
    re_path(r'^adm/mess/(?P<pk>\d+)/$',views.answer,name='answer'),
    re_path(r'^adm/declined/(?P<pk>\d+)/$',views.declined,name="declined"),
    re_path(r'^adm/acceptedrequst/$',views.acceptedbyadmin,name="accep"),
    re_path(r'^cancel/$',views.cancellation,name='can'),
    re_path(r'^cancelfinal/$',views.cancellation2,name='canc'),


]

