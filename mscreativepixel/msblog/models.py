from django.db import models

# Create your models here.
 
class HeaderNavs(models.Model):
    title  = models.CharField(max_length = 50)
    url    = models.CharField(max_length = 50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "HeaderNavs"