from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def Index(request):
    data = {}
    data['sub'] = ["HTML", "CSS", "jQuery", "Python", "Django"]
    data['dict'] = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    data['title'] = "我的第一个Python网站！"
    data['list']=map(str, range(100))  # 一个长度为100的 List
    return render(request,'index.html',data)
