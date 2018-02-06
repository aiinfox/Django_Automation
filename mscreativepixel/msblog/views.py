from django.shortcuts import render
from django.http import HttpResponse

from .models import HeaderNavs
from .models import Blogs
from django import template

register = template.Library()  

def index(request):

    blogs = Blogs.objects.all()
    context = {
        'homepage'  : True,
        'blogs'     : blogs
    }

    return render(request, 'msblog/index.html', context)

def about(request):
    return render(request, 'msblog/about.html')

def services(request):
    return render(request, 'msblog/service.html')

def work(request):
    return render(request, 'msblog/work.html')

def blog(request):
    return render(request, 'msblog/blog.html')

