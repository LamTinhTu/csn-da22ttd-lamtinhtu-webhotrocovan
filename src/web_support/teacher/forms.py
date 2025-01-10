from django import forms
from .models import CoVan, Lop, BoMon
from datetime import date


class CoVanForm(forms.ModelForm):
    LopQuanLy = forms.ModelChoiceField(
        queryset=Lop.objects.all(),
        label="Lớp đang quản lý",
        empty_label="Chọn lớp",
        required=False
    )
    bomon = forms.ModelChoiceField(
        queryset=BoMon.objects.all(),
        label= "Bộ môn",
        empty_label="Chọn bộ môn"
    )
    class Meta:
        model = CoVan
        fields = "__all__"
    def clean_birth_date(self):
        birth_date = self.cleaned_data['NgSinhCV']    
        birth_year = birth_date.year
        today = date.today()
        age = today.year - birth_year
        if age < 25:
            raise forms.ValidationError("Độ tuổi không hợp lệ.")
        return birth_date

class LopForm(forms.ModelForm):
    bomon = forms.ModelChoiceField(
        queryset=BoMon.objects.all(),
        label= "Bộ môn",
        empty_label="Chọn bộ môn"
    )
    class Meta:
        model = Lop
        fields = '__all__'
