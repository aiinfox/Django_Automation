from django.db import models
from datetime import datetime
import string, random
import uuid

# Create your models here.
 
class HeaderNavs(models.Model):
    title  = models.CharField(max_length = 50)
    url    = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "HeaderNavs"



class Blogs(models.Model):
    title               = models.CharField(max_length = 50)
    short_description   = models.TextField(max_length = 100)
    description         = models.TextField()
    created_at          = models.DateTimeField(default=datetime.now, blank=True)
    avatar              = models.ImageField(upload_to = 'static/img/avatar/', default = 'static/img/avatar_1.jpg')
    slug                = models.CharField(max_length=40, blank=True, default=uuid.uuid4, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"
