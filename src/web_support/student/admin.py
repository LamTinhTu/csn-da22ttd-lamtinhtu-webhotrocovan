from django.contrib import admin
from .models import SinhVien, XepLoai, sinhvien_xeploai
from common.utils import generate_recent_academic_years
from .forms import SinhVienForm, xeploaiform
from datetime import date
from django import forms
# Register your models here.
class sinhvienadmin(admin.ModelAdmin):
    form = SinhVienForm
    def get_fields(self, request, obj=None):
        # Nếu là thêm mới, hiển thị tất cả các trường
        if not obj:
            return ('MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'covan', 'lop')
        # Nếu chỉnh sửa, loại bỏ trường 'id'
        return ('HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'covan', 'lop')
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'NgSinhSV':
            min_year = 1960  # Giới hạn năm sinh thấp nhất
            max_year = date.today().year - 18  # Tính toán để đảm bảo đủ 18 tuổi
            kwargs['widget'] = forms.DateInput(attrs={
                'type': 'date',
                'min': f'{min_year}-01-01',  # Giới hạn ngày tối thiểu
                'max': f'{max_year}-01-01',  # Giới hạn ngày tối đa
            })
        return super().formfield_for_dbfield(db_field, request, **kwargs)

class XepLoaiSinhVienAdmin(admin.ModelAdmin):
    list_display = ('sinhvien', 'HocKyXL', 'NamXL', 'DiemTB', 'xeploai')
    fields = ('sinhvien', 'HocKyXL', 'NamXL', 'DiemTB')
    form = xeploaiform
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "NamXL":
            kwargs['choices'] = [(year, year) for year in generate_recent_academic_years()]
        if db_field.name == "HocKyXL":
            kwargs['choices'] = [('Học kỳ I', 'Học kỳ I'), ('Học kỳ II', 'Học kỳ II')]
        return super().formfield_for_choice_field(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        if obj.DiemTB >=3.6:
            obj.xeploai = XepLoai.objects.get(MaXL = 'XS')
        elif obj.DiemTB >=3.2:
            obj.xeploai = XepLoai.objects.get(MaXL = 'GI')
        elif obj.DiemTB >=2.5:
            obj.xeploai = XepLoai.objects.get(MaXL = 'KH')
        elif obj.DiemTB >=2.0:
            obj.xeploai = XepLoai.objects.get(MaXL = 'TB')
        elif obj.DiemTB >=1.0:
            obj.xeploai = XepLoai.objects.get(MaXL = 'YE')
        else:
            obj.xeploai = XepLoai.objects.get(MaXL = 'KE')
        super().save_model(request, obj, form, change)


admin.site.register(SinhVien, sinhvienadmin)
# admin.site.register(XepLoai)
admin.site.register(sinhvien_xeploai, XepLoaiSinhVienAdmin)