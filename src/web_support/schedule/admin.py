from django.contrib import admin
from .forms import lichhenform
from .models import LichHen
from datetime import date, timedelta
from django import forms
# Register your models here.
# class lichhenadmin(admin.ModelAdmin):
#     form = lichhenform
#     def get_fields(self, request, obj=None):
#         # Nếu là thêm mới, hiển thị tất cả các trường
#         if not obj:
#             return ('MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien')
#         # Nếu chỉnh sửa, loại bỏ trường 'id'
#         return ('TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien')
#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'NgayHen':
#             min_date = date.today() + timedelta(days=1)
#             max_date = min_date + timedelta(days = 365)
#             kwargs['widget'] = forms.DateInput(attrs={
#                 'type': 'date',
#                 'min': f'{min_date}',  # Giới hạn ngày tối thiểu
#                 'max': f'{max_date}',  # Giới hạn ngày tối đa
#             })
#         return super().formfield_for_dbfield(db_field, request, **kwargs)
# admin.site.register(LichHen, lichhenadmin)

