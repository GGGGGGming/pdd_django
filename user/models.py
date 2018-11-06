from django.db import models
from  company.models import companys
# Create your models here.

# class UserInfo(models.Model):
#     # id=models.AutoField(primary_key=True)#默认生成
#     account=models.CharField(max_length=30,primary_key=True)
#     password=models.CharField(max_length=30,null=False)
#     #0 表示一般用户 1表示HR
#     type=models.CharField(max_length=10,null=False,default='0',)
#     # sex=models.CharField(max_length=5,default='男')



class manager(models.Model):
    m_id=models.AutoField(primary_key=True)
    m_name=models.CharField(max_length=30,null=False)
    m_img=models.CharField(max_length=200)
    #管理人的职务
    m_position=models.CharField(max_length=50)
    #简介
    m_intro=models.TextField(max_length=1000)
    company = models.ForeignKey(companys, on_delete=models.CASCADE)