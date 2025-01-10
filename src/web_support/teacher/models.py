from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from homepage.models import User

# Create your models here.

class BoMon(models.Model):
    MaBM = models.CharField("Mã bộ môn", max_length=10, primary_key=True)
    TenBM = models.CharField("Tên bộ môn", max_length=50)

    class Meta:
        verbose_name = 'Bộ Môn'
        verbose_name_plural = 'Bộ Môn'

    def __str__(self):
        return self.TenBM
    

class CoVan(models.Model):
    MaCV = models.CharField("Mã cố vấn", max_length=10, primary_key=True)
    HoTenCV = models.CharField("Họ tên", max_length=50)
    NgSinhCV = models.DateField("Ngày Sinh")
    SDTCV = models.CharField("Số điện thoại", max_length=10)
    EmailCV = models.CharField("Email", max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='covans')
    LopQuanLy = models.CharField(max_length=10, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='covan', blank=True, null=True)

    class Meta:
        verbose_name = 'Cố vấn'
        verbose_name_plural = 'Cố vấn'

    def __str__(self):
        return self.HoTenCV[:50]
    
    def get_absolute_url(self):
        return reverse("cv_detail", kwargs={"pk": self.MaCV})
    
@receiver(post_save, sender=CoVan)
def create_user_for_sinhvien(sender, instance, created, **kwargs):
    if created:
        if not instance.user:
            user = User.objects.create_user(
                username=instance.MaCV,
                password=instance.NgSinhCV.strftime('%d%m%Y'),  # Định dạng ngày sinh làm mật khẩu (yyyyMMdd)
            )
            user.is_teacher = True
            user.save()
            instance.user = user
            instance.save()
    
class Lop(models.Model):
    MaLop = models.CharField("Mã lớp", max_length=10, primary_key=True)
    TenLop = models.CharField("Tên lớp", max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='lops')

    class Meta:
        verbose_name = 'Lớp'
        verbose_name_plural = 'Lớp'

    def __str__(self):
        return self.MaLop


