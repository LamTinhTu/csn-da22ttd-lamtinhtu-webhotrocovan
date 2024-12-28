# Generated by Django 5.1.4 on 2024-12-28 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XepLoai',
            fields=[
                ('MaXL', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('TenXL', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('MaSV', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('HoTenSV', models.CharField(max_length=50)),
                ('NgSinhSV', models.DateField(verbose_name='Ngày Sinh')),
                ('SDTSV', models.CharField(max_length=10)),
                ('EmailSV', models.CharField(max_length=50)),
                ('MatKhauSV', models.CharField(max_length=50)),
                ('covan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sinhviens', to='teacher.covan')),
                ('lop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sinhviens', to='teacher.lop')),
            ],
        ),
    ]