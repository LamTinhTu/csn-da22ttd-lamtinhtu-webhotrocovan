from django.db import models

# # Create your models here.from django.db import models
# from student.models import XepLoai
# from student.models import SinhVien
# from student.models import sinhvien_xeploai
# # Create your models here.
# class xeploaisinhvien(models.Model):
#     MaSV = models.CharField(max_length=10, primary_key=True)
#     HoTenSV = models.CharField(max_length=50)
#     Lop= models.CharField(max_length=10)
#     Diem = models.CharField(max_length=10)
#     NamXL = models.CharField(max_length=50)
#     HocKyXL = models.CharField(max_length=10)
#     TenXL = models.CharField(max_length=10)
    
#     class Meta:
#         verbose_name = 'Xếp Loại Sinh Viên'
#         verbose_name_plural = 'Xếp Loại Sinh Viên'

#     def _str_(self):
#         return self.MaSV
