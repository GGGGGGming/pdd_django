from django.conf.urls import url
from  . import  views
app_name='user'
urlpatterns = [


    url(r'^login\w*',views.login),
    url(r'^regist\w*',views.regist),
    url(r'^show\w*',views.showMessage),
    url(r"setcookie/",views.setcookie),
    url(r"getmanagerbyid/(?P<cid>\w+)",views.getManagerById),

]
