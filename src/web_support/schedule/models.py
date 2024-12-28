from django.db import models
from teacher.models import CoVan
from student.models import SinhVien
# Create your models here.
class LichHen(models.Model):
    MaH = models.CharField(max_length=10, primary_key=True)
    TenBuoiHen = models.CharField(max_length=50)
    NgayHen = models.DateField("Ngày Hẹn")
    GioHen = models.TimeField("Giờ Hẹn")
    DiaDiem = models.CharField(max_length=100)
    TrangThai = models.CharField(max_length=50)
    covan = models.ForeignKey(CoVan, on_delete=models.CASCADE, related_name='lichhens')
    SinhVien = models.ForeignKey(SinhVien, on_delete = models.CASCADE, related_name='lichhens')

    class Meta:
        verbose_name = 'Lịch Hẹn'
        verbose_name_plural = 'Lịch Hẹn'

    def _str_(self):
        return self.MaH