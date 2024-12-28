from django.db import models

# Create your models here.
    
class PhanQuyen(models.Model):
    MaPQ = models.CharField(max_length=10)
    TenPQ = models.CharField(max_length=20)

    def _str_(self):
        return self.MaPQ
    
class Admin(models.Model):
    MaAD = models.CharField(max_length=10)
    TaiKhoanAD = models.CharField(max_length=50)
    MatKhauAD = models.CharField(max_length=50)
    phanquyen = models.ForeignKey(PhanQuyen, on_delete= models.CASCADE, related_name = 'admins')

    def _str_(self):
        return self.MaAD