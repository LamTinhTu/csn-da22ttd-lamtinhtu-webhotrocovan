from django.db import models

# Create your models here.

class BoMon(models.Model):
    MaBM = models.CharField(max_length=10, primary_key=True)
    TenBM = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Bộ Môn'
        verbose_name_plural = 'Bộ Môn'

    def __str__(self):
        return self.TenBM
    

class CoVan(models.Model):
    MaCV = models.CharField(max_length=10, primary_key=True)
    HoTenCV = models.CharField(max_length=50)
    NgSinhCV = models.DateField("Ngày Sinh")
    SDTCV = models.CharField(max_length=10)
    EmailCV = models.CharField(max_length=50)
    MatKhauCV = models.CharField(max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='covans')

    class Meta:
        verbose_name = 'Cố vấn'
        verbose_name_plural = 'Cố vấn'

    def __str__(self):
        return self.HoTenCV[:50]
    
class Lop(models.Model):
    MaLop = models.CharField(max_length=10, primary_key=True)
    TenLop = models.CharField(max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='lops')

    class Meta:
        verbose_name = 'Lớp'
        verbose_name_plural = 'Lớp'

    def __str__(self):
        return self.MaLop


