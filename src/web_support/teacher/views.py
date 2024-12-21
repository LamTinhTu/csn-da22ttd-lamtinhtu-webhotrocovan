from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class teacher_view(TemplateView):
    template_name = "co_van/co_van.html"

class SinhVien_view(TemplateView):
    template_name = "sinh_vien/sinh_vien.html"

class XepLoai_view(TemplateView):
    template_name = "xep_loai/xep_loai.html"

class LichHen_view(TemplateView):
    template_name = "lich_hen/lich_hen.html"