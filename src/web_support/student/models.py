from django.db import models
from django.urls import reverse
from teacher.models import CoVan, Lop

# Create your models here.
  

class SinhVien(models.Model):
    MaSV = models.CharField("MSSV", max_length=10, primary_key=True, )
    HoTenSV = models.CharField("Họ tên", max_length=50)
    NgSinhSV = models.DateField("Ngày Sinh")
    SDTSV = models.CharField("Số điện thoại", max_length=10)
    EmailSV = models.CharField("Email", max_length=50)
    MatKhauSV = models.CharField("Mật khẩu", max_length=50)
    covan = models.ForeignKey(CoVan, on_delete=models.CASCADE, related_name='sinhviens')
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE, related_name='sinhviens')

    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'

    def __str__(self):
        return self.HoTenSV + " - " + self.MaSV
    def get_absolute_url(self):
        return reverse("sv_detail", kwargs={"pk": self.pk})
    
   

class XepLoai(models.Model):
    MaXL = models.CharField(max_length=10, primary_key=True)
    TenXL = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Xếp loại'
        verbose_name_plural = 'Xếp loại'

    def _str_(self):
        return self.MaXL
    

# class sinhvien_xeploai(models.Model):
#     sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='sv_xls')
#     xeploai = models.ForeignKey(XepLoai, on_delete=models.CASCADE, related_name='sv_xls')
#     NamXL = models.IntegerField()
#     HocKyXL = models.CharField(max_length=50)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['sinhvien', 'xeploai', 'NamXL', 'HocKyXL'], name='sv_xl')
#         ]

#     def _str_(self):
#         return self.NamXL + self.HocKyXL