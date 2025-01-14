from django import forms
from .models import LichHen
from teacher.models import CoVan
from student.models import SinhVien
from datetime import date, timedelta

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
    def clean_date(self):
        meet_day = self.cleaned_data['NgayHen']
        min_date = date.today() + timedelta(days=1)
        if meet_day < min_date:
            raise forms.ValidationError("Ngày hẹn không hợp lệ.")
        return meet_day
    class Meta:
        model = LichHen
        fields = "__all__"