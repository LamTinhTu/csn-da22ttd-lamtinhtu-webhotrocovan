from django import forms
from .models import CoVan, Lop, BoMon


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
        fields = ['MaCV', 'HoTenCV', 'NgSinhCV', 'SDTCV', 'EmailCV', 'bomon', 'LopQuanLy']