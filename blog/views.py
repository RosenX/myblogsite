# Create your views here.
#coding=utf-8

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from blog.models import Tag
from blog.models import Classification
from blog.models import Author
from blog.models import Comment
from blog.form import BlogAddForm
from blog.form import cmtAddForm
from django.http import Http404
from django.views.decorators import csrf

def blog_list(request,method='',id=''):
    blogs=[]
    if method and id:
        method=int(method)
        if method ==1:
            try:
                tag=Tag.objects.get(id=id)
            except Tag.DoesNotExist:
                raise Http404
            blogs = tag.blog_set.all()
        elif method==2:
            try:
                classification = Classification.objects.get(id=id)
            except Classification.DoesNotExist:
                raise Http404
            blogs =classification.blog_set.all()
        else:
            raise Http404
    elif method or id:
        raise Http404
    else:
        blogs = Blog.objects.all()
    tags = Tag.objects.all()
    classification=Classification.objects.all()
    blog_popular = Blog.objects.all().order_by('-visitedTime')[0:15]
    return render_to_response("blog_list.html", {"blogs": blogs,"tags":tags,
                                                 "blog_popular":blog_popular,
                                                 "classification":classification},
                               context_instance=RequestContext(request))

def blog_show(request, id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    comment = blog.comment_set.all().order_by('thread')
    blog.visitedTime=blog.visitedTime+1
    blog.save()
    tags = Tag.objects.all()
    classification=Classification.objects.all()
    blog_popular = Blog.objects.all().order_by('-visitedTime')[0:15]

    if request.method =='POST':
        form = cmtAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cmt = Comment(username=data['name'],email=data['email'],content=data['content'],blog=blog)
            father = data['thread']
            print father;
            if father:
                father_cmt = Comment.objects.get(id=father)
                father_cmt.sonCnt +=1
                father_cmt.save()
                cmt.thread =father_cmt.thread + '%4d'%father_cmt.sonCnt+'.'
            else:
                cmt.thread ='%4d'%(len(comment)+1)+'.'
            cmt.save()
            return HttpResponseRedirect('/blog/blog/%s/commentshow'%id)
        else:
            print "+++++++++++++++++hello+++++++++++++++"
            raise Http404
    else:
        form = cmtAddForm()
    return render_to_response("blog_show.html", {"blog": blog,"tags":tags,
                                                 "blog_popular":blog_popular,
                                                 "classification":classification,
                                                 "comment":comment,
                                                 "form":form,
                                                 "cmtlen":len(comment)},
                               context_instance=RequestContext(request))

@login_required
def blog_add(request):
    if request.method == 'POST':
        form = BlogAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tags =data['tag'].split()
            classification = data['classification']
            #添加类别
            Classification.objects.get_or_create(name=classification.strip())
            classification = Classification.objects.get(name=classification.strip())
            classification.count=classification.count+1
            classification.save()
            #创建博客
            blog = Blog(caption=data['caption'],content=data['content'],
                        classification=classification)
            blog.save()
            #添加作者
            Author.objects.get_or_create(user=request.user)
            author = Author.objects.get(user=request.user)
            blog.author.add(author)
            author.count = author.count+1
            author.save()
            #添加tag 先查询Tag表看是否有这个标签,没有创建
            for tag in tags:
                Tag.objects.get_or_create(tag_name=tag.strip())
            for tag in tags:
                theTag = Tag.objects.get(tag_name=tag.strip())
                blog.tags.add(theTag)
                theTag.count=theTag.count+1
                theTag.save()
            blog.save()
            
            id = Blog.objects.order_by('-publish_time')[0].id
            return HttpResponseRedirect('/blog/blog/%s'%id)
    else:
        form =BlogAddForm()
    return render_to_response('blog_add.html',{'form':form},
                             context_instance=RequestContext(request))

@login_required
def blog_edit(request,blogId=''):
    currentBlog=Blog.objects.get(id=blogId)
    old_tag = [obj.tag_name for obj in currentBlog.tags.all()]
    old_classification = currentBlog.classification.name
    if request.method == 'POST':
        form = BlogAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            currentBlog.caption=data['caption']
            currentBlog.content=data['content']
            #标签处理
            tags = data['tag'].split()            
            for tag in tags:tag = tag.strip()#去首尾空格
            for tag in tags:
                Tag.objects.get_or_create(tag_name=tag)
            currentBlog.tags=[]
            for tag in tags:
                theTag=Tag.objects.get(tag_name=tag)
                currentBlog.tags.add(theTag)
                theTag.count=theTag.count+1
                theTag.save()
            ##标签变化处理
            for oldtag in old_tag:
                theTag = Tag.objects.get(tag_name=oldtag)
                theTag.count=theTag.count-1
                theTag.save()
            #类别处理
            classification = data['classification'].strip()
            Classification.objects.get_or_create(name=classification)
            currentBlog.classification=Classification.objects.get(name=classification)
            currentBlog.classification.count=currentBlog.classification.count+1
            currentBlog.classification.save()
            currentBlog.save()
            #类别变化处理
            if old_classification != currentBlog.classification.name:
                classification = Classification.objects.get(name=old_classification)
                classification.count=classification.count-1
                classification.save()
            #作者添加
            return HttpResponseRedirect('/blog/blog/%s'%blogId)
    else:
        taglist=currentBlog.tags.all()
        initTagList=''
        if taglist:
            for tag in taglist:
                initTagList += str(tag)+' '
        form =BlogAddForm(
            initial={'caption':currentBlog.caption,
                     'content':currentBlog.content,
                     'tag':initTagList,
                     'classification':currentBlog.classification.name,
                    }
        )
        #form =BlogAddForm()
    return render_to_response('blog_add.html',{'form':form},
                             context_instance=RequestContext(request))

@login_required
def blog_del(request,blogId):
    currentBlog=Blog.objects.get(id=blogId)
    #处理统计数据：分类，标签，作者中的count
    # classification = currentBlog.classification
    # classification.count=classification.count-1
    # tags = currentBlog.tags.all()
    # for tag in tags:tag.count=tag.count-1
    for tag in currentBlog.tags.all():
        tag.count -=1
        tag.save()
    currentBlog.classification.count-=1
    currentBlog.classification.save()
    for author in currentBlog.author.all():
        author.count-=1
        author.save()
    currentBlog.delete()
    return HttpResponseRedirect('/blog/bloglist')

def blog_about(request):
    return render_to_response('about.html',context_instance=RequestContext(request))

def blog_home(request):
    return render_to_response('homepage.html',context_instance=RequestContext(request))

def blog_show_comment(request, id=''):
    blog=Blog.objects.get(id=id)
    comment=blog.comment_set.all().order_by('thread')
    return render_to_response('blog_comments_show.html', {"comment": comment,
                                                          "cmtlen":len(comment)})

