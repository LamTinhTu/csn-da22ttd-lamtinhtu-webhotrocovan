from django.db import models

# Create your models here.

class BoMon(models.Model):
    MaBM = models.CharField(max_length=10)
    TenBM = models.CharField(max_length=50)

    def _str_(self):
        return self.MaBM
    

class CoVan(models.Model):
    MaCV = models.CharField(max_length=10)
    HoTenCV = models.CharField(max_length=50)
    NgSinhCV = models.DateField("Ngày Sinh")
    SDTCV = models.CharField(max_length=10)
    EmailCV = models.CharField(max_length=50)
    MatKhauCV = models.CharField(max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='covans')

    def _str_(self):
        return self.MaCV
    
class Lop(models.Model):
    MaLop = models.CharField(max_length=10)
    TenLop = models.CharField(max_length=50)
    bomon = models.ForeignKey(BoMon, on_delete=models.CASCADE, related_name='lops')

    def _str_(self):
        return self.MaLop
    

class SinhVien(models.Model):
    MaSV = models.CharField(max_length=10)
    HoTenSV = models.CharField(max_length=50)
    NgSinhSV = models.DateField("Ngày Sinh")
    SDTSV = models.CharField(max_length=10)
    EmailSV = models.CharField(max_length=50)
    MatKhauSV = models.CharField(max_length=50)
    covan = models.ForeignKey(CoVan, on_delete=models.CASCADE, related_name='sinhviens')
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE, related_name='sinhviens')

    def _str_(self):
        return self.MaSV
    
class LichHen(models.Model):
    MaH = models.CharField(max_length=10)
    TenBuoiHen = models.CharField(max_length=50)
    NgayHen = models.DateField("Ngày Hẹn")
    GioHen = models.TimeField("Giờ Hẹn")
    DiaDiem = models.CharField(max_length=100)
    TrangThai = models.CharField(max_length=50)
    covan = models.ForeignKey(CoVan, on_delete=models.CASCADE, related_name='lichhens')
    SinhVien = models.ForeignKey(SinhVien, on_delete = models.CASCADE, related_name='lichhens')

    def _str_(self):
        return self.MaH
    

class XepLoai(models.Model):
    MaXL = models.CharField(max_length=10)
    TenXL = models.CharField(max_length=10)

    def _str_(self):
        return self.MaXL
    

class sinhvien_xeploai(models.Model):
    sinhvien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='sv_xls')
    XepLoai = models.ForeignKey(XepLoai, on_delete=models.CASCADE, related_name='sv_xls')
    NamXL = models.IntegerField()
    HocKyXL = models.CharField(max_length=50)

    def _str_(self):
        return self.NamXL + self.HocKyXL
    
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
