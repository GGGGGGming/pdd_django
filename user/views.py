from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import  models
from  django.core.serializers import  serialize
import  json
# Create your views here.
'''
此模块方法未测试
仅供参考
建议负责人重写

此模块 设计关于所有的人员信息和
操作

'''
#登录
def login(request):
    print( request.method)
    # if request.method == 'POST':
    if request.method == 'POST':
        # user = json.loads(request.body)
        # id=user['telephone']
        # password=user['password']
        # print(id)
        # print(password)
        # if id=="15776554504" and password=="123456":
        content={"statuscode":201}
        resp=HttpResponse(json.dumps(content),status=200, charset='utf-8', content_type='application/json')

        resp['token']="this is token!"
        resp['Access-Control-Expose-Headers']='token'
        # print(resp.serialize_headers())
        # resp.set_cookie('h1', '你好'.encode('utf8'), max_age=1111)
        resp.set_cookie("SSS", "python2")
            # print(resp)

        #
        if request.method=='POST':
          user=models.UserInfo.objects.filter(name='fj')
          print(user) #<QuerySet [<UserInfo: UserInfo object (3)>]>

          print(list(user)[0])
          #将set 转化为list 再取出第一个元素（对象）
          if list(user)[0].password=='123':
              return resp


          else:
             return HttpResponse("402")


    else:
        return HttpResponse("404")
        # tel=request.META['telephone']
        # password=request.META["password"]
        # if tel=="15776554504" and password=="123456":
        #     return HttpResponse({"statuscode":"201"})
        # else:
        #     return HttpResponse("404")

#注册
def regist(request):
    if request.method=='POST':
        data=json.loads(request.body)
        # name=data['name']
        # password=data['password']
        # user={
        #     "name":name,
        #     "password":password
        #
        # }
        res=models.UserInfo.objects.create(**data)
        print(res)

        return HttpResponse('<h2>这里是注册</h2>')

    else:


        return HttpResponse("{'statecode':400}")

#显示个人信息
def showMessage(reauest):

    return HttpResponse({'status':'200'})

#设置cookie
def setcookie(request):
    res = HttpResponse()
    cookie = res.set_cookie("sunck","nice")
    return res

#获取公司管理团队的信息(测试通过勿修改)
def getManagerById(request,cid):
    managers=[]
    #从mysql取出来的是str 要把外边的双引号去掉恢复为原来的数据格式
    data_mangers=eval(serialize('json',list(models.manager.objects.filter(c_id=cid)),ensure_ascii=False))
    #这里因为数据是从model里取出来，所以取出来的数据是model对象，取其中需要的数据fields (字段)
    for m in data_mangers:

        managers.append(m['fields'])
    print(managers)
    #发送给前端
    return HttpResponse(json.dumps(managers))


