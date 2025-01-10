from django import forms
from .models import LichHen
from teacher.models import CoVan
from student.models import SinhVien
from datetime import date

class lichhenform(forms.ModelForm):
    sinhvien = forms.ModelChoiceField(
        queryset=SinhVien.objects.all(),
        label= "Sinh Viên",
        empty_label="Chọn Sinh Viên"
    )
    covan = forms.ModelChoiceField(
        queryset=CoVan.objects.all(),
        label= "Cố Vấn",
        empty_label="Chọn cố vấn"
    )
    class Meta:
        model = LichHen
        fields = "__all__"