from django import forms
from .models import SinhVien, sinhvien_xeploai
from teacher.models import CoVan, Lop
from datetime import date


class SinhVienForm(forms.ModelForm):
    lop = forms.ModelChoiceField(
        queryset=Lop.objects.all(),
        label= "Lớp",
        empty_label="Chọn lớp"
    )
    covan = forms.ModelChoiceField(
        queryset=CoVan.objects.all(),
        label= "Cố Vấn ",
        empty_label="Chọn Cố Vấn"
    )
    class Meta:
        model = SinhVien
        fields = "__all__"
    def clean_birth_date(self):
        birth_date = self.cleaned_data['NgSinhSV']    
        birth_year = birth_date.year
        today = date.today()
        age = today.year - birth_year
        if age < 18:
            raise forms.ValidationError("Độ tuổi không hợp lệ.")
        return birth_date

class xeploaiform(forms.ModelForm):
    sinhvien = forms.ModelChoiceField(
        queryset=SinhVien.objects.all(),
        label= "Sinh Viên",
        empty_label="Chọn Sinh Viên"
    )
    class Meta:
        model = sinhvien_xeploai
        fields = "__all__"