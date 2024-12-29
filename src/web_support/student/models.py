from django.db import models
from django.urls import reverse
from teacher.models import CoVan, Lop
from homepage.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class SinhVien(models.Model):
    MaSV = models.CharField("MSSV", max_length=10, primary_key=True)
    HoTenSV = models.CharField("Họ tên", max_length=50)
    NgSinhSV = models.DateField("Ngày Sinh")
    SDTSV = models.CharField("Số điện thoại", max_length=10)
    EmailSV = models.CharField("Email", max_length=50)
    MatKhauSV = models.CharField("Mật khẩu", max_length=50)
    covan = models.ForeignKey(CoVan, on_delete=models.CASCADE, related_name='sinhviens')
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE, related_name='sinhviens')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='sinhvien', blank=True, null=True)

    class Meta:
        verbose_name = 'Sinh viên'
        verbose_name_plural = 'Sinh viên'

    def __str__(self):
        return f"{self.HoTenSV} - {self.MaSV}"

    def get_absolute_url(self):
        return reverse("sv_detail", kwargs={"pk": self.MaSV})

@receiver(post_save, sender=SinhVien)
def create_user_for_sinhvien(sender, instance, created, **kwargs):
    if created:
        # Tạo user cho sinh viên nếu chưa có
        if not instance.user:
            user = User.objects.create_user(
                username=instance.MaSV,
                password=instance.NgSinhSV.strftime('%Y%m%d'),  # Định dạng ngày sinh làm mật khẩu (yyyyMMdd)
            )
            user.is_student = True
            user.save()
            instance.user = user
            instance.save()

class XepLoai(models.Model):
    MaXL = models.CharField(max_length=10, primary_key=True)
    TenXL = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Xếp loại'
        verbose_name_plural = 'Xếp loại'

    def __str__(self):
        return self.TenXL


class sinhvien_xeploai(models.Model):
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='sv_xls')
    xeploai = models.ForeignKey(XepLoai, on_delete=models.CASCADE, related_name='sv_xls')
    NamXL = models.CharField(max_length=50)
    HocKyXL = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sinhvien', 'xeploai', 'NamXL', 'HocKyXL'], name='unique_sv_xl')
        ]
        verbose_name = 'Sinh viên xếp loại'
        verbose_name_plural = 'Sinh viên xếp loại'

    def __str__(self):
        return f"{self.sinhvien} - {self.xeploai} - Năm: {self.NamXL} - Học kỳ: {self.HocKyXL}"
