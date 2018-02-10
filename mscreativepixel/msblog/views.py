from django.shortcuts import render
from django.http import HttpResponse

from .models import HeaderNavs
from .models import Blogs

#Home Page
def index(request):

    blogs = Blogs.objects.all()
    context = {
        'homepage'  : True,
        'blogs'     : blogs
    }

    return render(request, 'msblog/index.html', context)

#About
def about(request):
    return render(request, 'msblog/about.html')

#Services
def services(request):
    return render(request, 'msblog/service.html')

#Work
def work(request):
    return render(request, 'msblog/work.html')

#Blog
def blog(request):

    blogs = Blogs.objects.all()
    context = {
        'blogs' : blogs
    }

    return render(request, 'msblog/blog.html', context)

#Blog Detail
def blogdetail(request, slug):

    post  = Blogs.objects.get(slug=slug)
    blogs = Blogs.objects.all()
    context = {
        'post'  : post,
        'blogs' : blogs
    }

    return render(request, 'msblog/blog-detail.html', context)

