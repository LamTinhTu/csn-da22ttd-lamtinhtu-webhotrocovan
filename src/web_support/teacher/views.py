from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from student.models import SinhVien
from .models import CoVan, Lop, BoMon
from schedule.models import LichHen
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random

# Create your views here.
class teacher_view(TemplateView):
    template_name = "co_van/co_van.html"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
        except CoVan.DoesNotExist:
            return redirect('login')
        return context

class SinhVien_view(TemplateView):
    template_name = "sinh_vien/sinh_vien.html"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            ds_sinhvien = covan.sinhviens.all()
            context['ds_sinhvien'] = ds_sinhvien
        except CoVan.DoesNotExist:
            return redirect('login')
        return context

class XepLoai_view(TemplateView):
    template_name = "xep_loai/xep_loai.html"

class LichHen_view(TemplateView):
    template_name = "lich_hen/lich_hen.html"

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            ds_lichhen = covan.lichhens.all()
            context['ds_lichhen'] = ds_lichhen
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
class TC_SCD_Create(CreateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'SinhVien']
    template_name = "lich_hen/create.html"
    success_url = reverse_lazy('lich_hen')

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            ds_sinhvien = covan.sinhviens.all()
            context['ds_sinhvien'] = ds_sinhvien
            so_ngau_nhien = random.randint(0, 99999999)
            MaLH = f"LH{so_ngau_nhien:08d}"
            context['MaLH'] = MaLH
        except CoVan.DoesNotExist:
            return redirect('login')
        return context

class TC_SCD_Edit(TemplateView):
    template_name = "lich_hen/lh_edit.html"



class SinhVien_create(CreateView):
    model = SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'MatKhauSV', 'covan', 'lop']
    template_name = "sinh_vien/sv_create.html"
    success_url = reverse_lazy('sinh_vien')

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            context['ds_lop'] = Lop.objects.all()
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
class SinhVien_edit(UpdateView):
    model = SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'MatKhauSV', 'covan', 'lop']
    template_name = "sinh_vien/sv_edit.html"
    success_url = reverse_lazy('sinh_vien')
    context_object_name = "sinhvien"

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            context['ds_lop'] = Lop.objects.all()
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
class Covan_edit(UpdateView):
    model = CoVan
    fields = ['MaCV', 'HoTenCV', 'NgSinhCV', 'SDTCV', 'EmailCV', 'MatKhauCV', 'bomon']
    template_name = "co_van/update.html"
    success_url = reverse_lazy('co_van')
    context_object_name = "covan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # Lấy người dùng hiện tại
        covan = CoVan.objects.get(user=user)
        context['covan'] = covan
        context['lops'] = Lop.objects.all()
        context['bomons'] = BoMon.objects.all()      
        return context

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Đăng xuất người dùng
        return redirect('login')