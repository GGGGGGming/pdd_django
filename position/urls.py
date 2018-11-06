from  django.conf.urls import url

from . import  views

app_name='position'

urlpatterns=[

    #通过条件获取所有岗位
    url(r'getjob\w*/(?P<index>\d*)/(?P<con>\w*)/',views.getPositionsByCon,name='getjob'),


    #获取页码
    url(r'getPage\w*/(?P<con>\w*)/',views.getPage,name='getPage'),


    # 获取岗位
    url(r'getpositions/',views.getPositions),


    # 获取公司标签
    url(r'getlals/',views.gteLals),

    #保存数据（mongodb 到 mysql  ）
    url('save',views.Save),


]
