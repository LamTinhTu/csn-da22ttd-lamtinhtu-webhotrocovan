# Generated by Django 5.1.4 on 2025-01-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien_xeploai',
            name='HocKyXL',
            field=models.CharField(choices=[('Học kỳ I', 'Học kỳ I'), ('Học kỳ II', 'Học kỳ II')], max_length=50, verbose_name='Học kỳ'),
        ),
    ]