from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from student.models import SinhVien
from .models import CoVan, Lop

# Create your views here.
class teacher_view(TemplateView):
    template_name = "co_van/co_van.html"

class SinhVien_view(ListView):
    model = SinhVien
    context_object_name = "SinhViens"
    template_name = "sinh_vien/sinh_vien.html"

class XepLoai_view(TemplateView):
    template_name = "xep_loai/xep_loai.html"

class LichHen_view(TemplateView):
    template_name = "lich_hen/lich_hen.html"

class SinhVien_create(CreateView):
    model = SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'MatKhauSV', 'covan', 'lop']
    template_name = "sinh_vien/sv_create.html"
    success_url = reverse_lazy('sinh_vien')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lops'] = Lop.objects.all()     
        context['covans'] = CoVan.objects.all()  
         
        return context