from . import views
from django.urls import re_path



urlpatterns = [
    re_path(r'^contact/submit/$',views.messaging,name="messaging"),
    re_path(r'^adm/contactinfo/$',views.contactinfo,name="contactinfo"),
    re_path(r'^adm/contactinfo/del/(?P<pk>\d+)/$',views.contact_del,name="contactdel"),
]