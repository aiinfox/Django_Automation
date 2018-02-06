from django.db import models
from datetime import datetime

# Create your models here.
 
class HeaderNavs(models.Model):
    title  = models.CharField(max_length = 50)
    url    = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "HeaderNavs"



class Blogs(models.Model):
    title           = models.CharField(max_length = 50)
    description     = models.TextField(max_length = 200)
    created_at      = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"
