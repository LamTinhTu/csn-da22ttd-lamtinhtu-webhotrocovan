from django.contrib import admin
from .forms import lichhenform
from .models import LichHen
# Register your models here.
class lichhenadmin(admin.ModelAdmin):
    form = lichhenform
    def get_fields(self, request, obj=None):
        # Nếu là thêm mới, hiển thị tất cả các trường
        if not obj:
            return ('MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien')
        # Nếu chỉnh sửa, loại bỏ trường 'id'
        return ('TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien')
admin.site.register(LichHen, lichhenadmin)

