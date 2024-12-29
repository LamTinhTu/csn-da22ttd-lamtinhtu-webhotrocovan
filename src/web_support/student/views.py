from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView
from student.models import SinhVien
from teacher.models import CoVan
from schedule.models import LichHen
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random

# Create your views here.

class student_view(TemplateView):
    template_name = "sinhvien/sv_Sinhvien.html"
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            sinhvien = SinhVien.objects.get(user=user)
            context['sinhvien'] = sinhvien  # Truyền đối tượng sinh viên vào context
            covan = sinhvien.covan
            context['covan'] = covan
        except SinhVien.DoesNotExist:
            return redirect('login')
        return context

class student_detail(DetailView):
    model = SinhVien
    template_name = "sinhvien/sv_detail.html"
    context_object_name = "sinhvien"
    
class Student_edit(TemplateView):
    template_name = "sinhvien/sv_edit.html"

class student_teacher_view(TemplateView):
    template_name = "covan/sv_covan.html"
    
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user  # Lấy người dùng hiện tại
        try:
            sinhvien = SinhVien.objects.get(user=user)
            covan = sinhvien.covan
            context['covan'] = covan
        except SinhVien.DoesNotExist:
            context['error'] = 'Không tìm thấy sinh viên'
        return context

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Đăng xuất người dùng
        return redirect('login')

class student_xeploai_view(TemplateView):
    template_name = "xeploai/sv_xeploai.html"

class student_lichhen_view(TemplateView):
    template_name = "lichhen/sv_lichhen.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        try:
            sinhvien = SinhVien.objects.get(user=user)
            ds_lichhen = sinhvien.lichhens.all()
            context['ds_lichhen'] = ds_lichhen
        except SinhVien.DoesNotExist:
            context['error'] = 'Không tìm thấy sinh viên'
        return context
class ST_SCD_Create(CreateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'SinhVien']
    template_name = "lichhen/create.html"
    success_url = reverse_lazy('lichhen')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        try:
            sinhvien = SinhVien.objects.get(user=user)
            ds_lichhen = sinhvien.lichhens.all()
            context['sinhvien'] = sinhvien
            covan = sinhvien.covan
            context['covan'] = covan
            context['ds_lichhen'] = ds_lichhen
            so_ngau_nhien = random.randint(0, 99999999)
            MaLH = f"LH{so_ngau_nhien:08d}"
            context['MaLH'] = MaLH
        except SinhVien.DoesNotExist:
            context['error'] = 'Không tìm thấy sinh viên'
        return context
    
class ST_SCD_Edit(TemplateView):
    template_name = "lichhen/lh_edit.html"