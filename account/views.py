# Create your views here.

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user =auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('blog/bloglist')
        else:
            return response("Your username and password don't match")
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))

