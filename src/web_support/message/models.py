from django.db import models
from homepage.models import User

# Create your models here.
class ThongBao(models.Model):
    Ngay = models.DateField("Ngày")
    Gio = models.TimeField("Giờ")
    TieuDe = models.CharField("Tiêu đề", max_length=100)
    NoiDung = models.CharField("Nội dung thông báo", max_length=450)
    TrangThaiTB = models.CharField("Trạng thái", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thongbaos')

    def __str__(self):
        return self.TieuDe + self.Ngay + self.Gio