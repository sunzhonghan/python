from django.http import HttpResponse
from blog.models import news

def add(request):
    firstnews = news()
    firstnews.title = "我的第一个博文"
    firstnews.content = "内容是什么不知道会不会乱码！"
    firstnews.save()
    return HttpResponse("添加成功！")

