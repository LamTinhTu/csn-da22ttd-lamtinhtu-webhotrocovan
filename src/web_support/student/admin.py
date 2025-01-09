from django.contrib import admin
from .models import SinhVien, XepLoai, sinhvien_xeploai
from common.utils import generate_recent_academic_years
# Register your models here.
class sinhvienadmin(admin.ModelAdmin):
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'covan', 'lop']

class XepLoaiSinhVienAdmin(admin.ModelAdmin):
    list_display = ('sinhvien', 'HocKyXL', 'NamXL', 'DiemTB', 'xeploai')
    fields = ('sinhvien', 'HocKyXL', 'NamXL', 'DiemTB')

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
admin.site.register(XepLoai)
admin.site.register(sinhvien_xeploai, XepLoaiSinhVienAdmin)