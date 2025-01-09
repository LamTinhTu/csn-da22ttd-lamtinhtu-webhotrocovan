from django.contrib import admin
from .models import BoMon, Lop, CoVan
from .forms import CoVanForm
# Register your models here.
class CoVanAdmin(admin.ModelAdmin):
    form = CoVanForm

admin.site.register(BoMon)
admin.site.register(CoVan, CoVanAdmin)
admin.site.register(Lop)