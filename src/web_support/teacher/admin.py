from django.contrib import admin
from django import forms
from .models import BoMon, Lop, CoVan
from .forms import CoVanForm, LopForm
from datetime import date
# Register your models here.
class CoVanAdmin(admin.ModelAdmin):
    form = CoVanForm
    def get_fields(self, request, obj=None):
        # Nếu là thêm mới, hiển thị tất cả các trường
        if not obj:
            return ('MaCV', 'HoTenCV', 'NgSinhCV', 'SDTCV', 'EmailCV', 'bomon', 'LopQuanLy')
        # Nếu chỉnh sửa, loại bỏ trường 'id'
        return ('HoTenCV', 'NgSinhCV', 'SDTCV', 'EmailCV', 'bomon', 'LopQuanLy')
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'NgSinhCV':
            min_year = 1960  # Giới hạn năm sinh thấp nhất
            max_year = date.today().year - 25  # Tính toán để đảm bảo đủ 18 tuổi
            kwargs['widget'] = forms.DateInput(attrs={
                'type': 'date',
                'min': f'{min_year}-01-01',  # Giới hạn ngày tối thiểu
                'max': f'{max_year}-01-01',  # Giới hạn ngày tối đa
            })
        return super().formfield_for_dbfield(db_field, request, **kwargs)

class LopAdmin(admin.ModelAdmin):
    form = LopForm
    def get_fields(self, request, obj=None):
        # Nếu là thêm mới, hiển thị tất cả các trường
        if not obj:
            return ('MaLop', 'TenLop', 'bomon')
        # Nếu chỉnh sửa, loại bỏ trường 'id'
        return ('TenLop', 'bomon')
    
class BoMonAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        # Nếu là thêm mới, hiển thị tất cả các trường
        if not obj:
            return ('MaBM', 'TenBM')
        # Nếu chỉnh sửa, loại bỏ trường 'id'
        return ('TenBM',)

admin.site.register(BoMon, BoMonAdmin)
admin.site.register(CoVan, CoVanAdmin)
admin.site.register(Lop, LopAdmin)