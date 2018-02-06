from django.contrib import admin

# Register your models here.

from .models import HeaderNavs
from .models import Blogs

admin.site.register(HeaderNavs)
admin.site.register(Blogs)
