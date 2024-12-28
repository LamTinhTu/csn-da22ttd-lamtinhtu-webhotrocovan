from django.contrib import admin

# Register your models here.
from .models import Admin, PhanQuyen
admin.site.register(PhanQuyen)
admin.site.register(Admin)