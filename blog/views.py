#coding=utf8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from blog.models import Article, ArticleQueryset, Tag, Comment, BugTalk, BugTalkInline
from django import forms
from django.http import JsonResponse

def BlogIndex(request):
    blog_list = Article.objects.published()
    tags = Tag.objects.all()
    newBlog = Article.objects.published()[:3]
    return render(request, 'blog/index.html', {'blog_list': blog_list, 'tags': tags, 'newBlog': newBlog})

def blogDetail(request, blog_id):
    try:
        blog = Article.objects.get(pk = blog_id)
    except Article.DoesNotExist:
        raise Http404
    tags = Tag.objects.all()
    newBlog = Article.objects.published()[:3]
    return render(request, 'blog/blog2.html', {'blog': blog, 'tags': tags, 'newBlog': newBlog})

def tag(request, tag_id):
    try:
        blogs = Tag.objects.get(pk = tag_id)
    except Tag.DoesNotExist:
        raise Http404
    tags = Tag.objects.all()
    newBlog = Article.objects.published()[:3]
    return render(request, 'blog/tag.html', {'blogs': blogs, 'tags': tags, 'newBlog': newBlog})

def blog_show_comment(request, blog_id):
    blog = Article.objects.get(pk=blog_id)
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        print name, content
        try:
            new_comment = Comment()
            new_comment.article = blog
            new_comment.name = name
            new_comment.content = content
            new_comment.save()
            import datetime
            date = unicode(datetime.datetime.now())[0:-13]                  #TODO datatype优化
            date = u' ' + date
            data_returned = {"name": name, "content": content, "date": date}
        except Exception, ex:
            print ex
            return HttpResponse("false")

        return JsonResponse(data_returned)

    return render(request, 'blog/blog_comments_show.html', {'blog': blog})

def bug_talk(request):
    tags = Tag.objects.all()
    newBlog = Article.objects.published()[:3]
    bugs = BugTalk.objects.all()
    return render(request, 'blog/bug_talk.html', {'tags': tags, 'newBlog': newBlog, 'bugs': bugs})

def jqtest(request):
    return render(request, 'blog/jqtest.html', {})

def jqget(request):
    return HttpResponse("test")
def jqpost(request):

    if request.method == 'POST':
        print "it's a test of post"
        name =  request.POST['name']
        city = request.POST['city']
        strReturnToclient = "my name is: " + name + " and I live in " + city
        return HttpResponse(strReturnToclient)
    else:
        return HttpResponse("post")

def bug_submit(request):
    if request.method == 'POST':
        try:
            bugs = BugTalk.objects.all()
            new_bug = BugTalk()
            new_bug.nick_name = request.POST['name']
            new_bug.content = request.POST['content']
            new_bug.save()
            print new_bug.nick_name
        except Exception, ex:
            return HttpResponse("false")
        return render(request, 'blog/bug_submit.html', {'bugs': bugs})
    else:
        return HttpResponse("<h1>test</h1>")

def bug_submit_inline(request):
    if request.method == 'POST':
        print request.POST
        data_return = {}
        try:
            type = request.POST['type']
            parent_bug = request.POST['parent_bug']
            name = request.POST['name']
            content = request.POST['content']
        except KeyError, ex:
            print ex
            return HttpResponse("false")
        try:
            parent_bug_object = BugTalk.objects.get(id=int(parent_bug))
        except BugTalk.DoesNotExist, ex:
            print ex
            return HttpResponse("false")
        name_pre = ""
        if int(type) == 0:
            name_pre = parent_bug_object.nick_name
        elif int(type) == 1:
            try:
                comment_bug = request.POST['comment_bug']
                comment_bug_object = BugTalkInline.objects.get(id=int(comment_bug))
            except (KeyError, BugTalkInline.DoesNotExist), ex:
                print ex
                return HttpResponse("false")
            name_pre = comment_bug_object.nick_name

        try:
            comment_bug = BugTalkInline()
            comment_bug.bug_pre = parent_bug_object
            comment_bug.name_pre = name_pre
            comment_bug.nick_name = name
            comment_bug.content = content
            comment_bug.save()
        except BaseException , ex:
            print ex;
            return HttpResponse("false")
        import pytz
        pub_date = unicode(comment_bug.pub_data)[0:-16]                #TODO datatime优化
        data_return = {"comment_id": comment_bug.id,
                        "name_pre": name_pre, "nick_name": name, "bug_id": parent_bug, "content": content,
                        "pub_date": pub_date}
        print data_return
        return JsonResponse(data_return)
    return HttpResponse("test")
def jqform(request):
    return HttpResponse("it's a test of jqform")


import json
def comments_upload(request):
    if request.method == 'POST':
        print "it's a test"

        name = request.POST['name']
        password = request.POST['password']
        print name, password
        return_dict = {'name': name, 'password':password}
        return JsonResponse(return_dict)
    else:
        return HttpResponse("<h1>test</h1>")

def test_modal(request):
    return render(request, "blog/modal.html", {})

#TODO 分页
#TODO 数据库查询优化
#TODO 多级评论模块完善
#TODO datatime优化
#TODO delete ALL test tiles

