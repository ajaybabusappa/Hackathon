from django.contrib import admin

# Register your models here.
from . models import courses,file
admin.site.register(courses)
admin.site.register(file)