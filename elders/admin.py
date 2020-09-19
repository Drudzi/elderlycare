from django.contrib import admin

# Register your models here.
from .models import Elder, Log

admin.site.register(Elder)
admin.site.register(Log)