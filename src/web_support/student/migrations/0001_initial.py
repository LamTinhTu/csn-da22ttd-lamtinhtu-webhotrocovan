# Generated by Django 5.1.4 on 2025-01-12 16:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='XepLoai',
            fields=[
                ('MaXL', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TenXL', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Xếp loại',
                'verbose_name_plural': 'Xếp loại',
            },
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('MaSV', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='MSSV')),
                ('HoTenSV', models.CharField(max_length=50, verbose_name='Họ tên')),
                ('NgSinhSV', models.DateField(verbose_name='Ngày Sinh')),
                ('SDTSV', models.CharField(max_length=10, verbose_name='Số điện thoại')),
                ('EmailSV', models.CharField(max_length=50, verbose_name='Email')),
                ('covan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinhviens', to='teacher.covan')),
                ('lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sinhviens', to='teacher.lop')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sinhvien', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sinh viên',
                'verbose_name_plural': 'Sinh viên',
            },
        ),
        migrations.CreateModel(
            name='sinhvien_xeploai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NamXL', models.CharField(choices=[('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024'), ('2024-2025', '2024-2025'), ('2025-2026', '2025-2026')], max_length=50, verbose_name='Năm Học')),
                ('HocKyXL', models.CharField(choices=[('Học kỳ I', 'Học kỳ I'), ('Học kỳ II', 'Học kỳ II')], max_length=50, verbose_name='Học kỳ')),
                ('DiemTB', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Điểm trung bình')),
                ('sinhvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sv_xls', to='student.sinhvien')),
                ('xeploai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sv_xls', to='student.xeploai')),
            ],
            options={
                'verbose_name': 'Xếp loại sinh viên',
                'verbose_name_plural': 'Xếp loại sinh viên',
                'unique_together': {('sinhvien', 'NamXL', 'HocKyXL')},
            },
        ),
    ]
