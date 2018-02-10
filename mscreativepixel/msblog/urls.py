from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('work', views.work, name='work'),
    path('blog', views.blog, name='blog'),
    path('blogdetail:<slug:slug>', views.blogdetail, name='blogdetail')
]