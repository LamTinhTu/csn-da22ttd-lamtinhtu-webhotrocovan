from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from student.models import SinhVien, sinhvien_xeploai, XepLoai
from .models import CoVan, Lop, BoMon
from schedule.models import LichHen
from message.models import ThongBao
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from common.utils import generate_recent_academic_years
import random
import datetime
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
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            ds_xeploai = sinhvien_xeploai.objects.filter(sinhvien__covan = covan)
            context['ds_xeploai'] = ds_xeploai
        except CoVan.DoesNotExist:
            return redirect('login')
        return context

class XepLoai_CreateView(CreateView):
    model = sinhvien_xeploai
    fields = ['sinhvien', 'NamXL', 'HocKyXL', 'DiemTB', 'xeploai']
    template_name = "xep_loai/xl_create.html"
    success_url = reverse_lazy('xep_loai')

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            ds_sinhvien = covan.sinhviens.all()
            context['ds_sinhvien'] = ds_sinhvien
            context['ds_namhoc'] = generate_recent_academic_years()
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)

        if instance.DiemTB >= 3.6:
            instance.xeploai = XepLoai.objects.get(MaXL = 'XS')
        elif instance.DiemTB >= 3.2:
            instance.xeploai = XepLoai.objects.get(MaXL = 'GI')
        elif instance.DiemTB >= 2.5:
            instance.xeploai = XepLoai.objects.get(MaXL = 'KH')
        elif instance.DiemTB >= 2.0:
            instance.xeploai = XepLoai.objects.get(MaXL = 'TB')
        elif instance.DiemTB >= 1.0:
            instance.xeploai = XepLoai.objects.get(MaXL = 'YE')
        else:
            instance.xeploai = XepLoai.objects.get(MaXL = 'KE')
        
        instance.save()
        return super().form_valid(form)
    
class XepLoai_EditView(UpdateView):
    model = sinhvien_xeploai
    fields = ['sinhvien', 'NamXL', 'HocKyXL', 'DiemTB', 'xeploai']
    template_name = "xep_loai/xl_edit.html"
    success_url = reverse_lazy('xep_loai')
    context_object_name = 'xeploai'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            ds_sinhvien = covan.sinhviens.all()
            context['ds_sinhvien'] = ds_sinhvien
            context['ds_namhoc'] = generate_recent_academic_years()
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)

        if instance.DiemTB >= 3.6:
            instance.xeploai = XepLoai.objects.get(MaXL = 'XS')
        elif instance.DiemTB >= 3.2:
            instance.xeploai = XepLoai.objects.get(MaXL = 'GI')
        elif instance.DiemTB >= 2.5:
            instance.xeploai = XepLoai.objects.get(MaXL = 'KH')
        elif instance.DiemTB >= 2.0:
            instance.xeploai = XepLoai.objects.get(MaXL = 'TB')
        elif instance.DiemTB >= 1.0:
            instance.xeploai = XepLoai.objects.get(MaXL = 'YE')
        else:
            instance.xeploai = XepLoai.objects.get(MaXL = 'KE')
        
        instance.save()
        return super().form_valid(form)
    
def xeploai_delete(request, pk):
    obj = sinhvien_xeploai.objects.filter(pk=pk)
    obj.delete()
    return redirect("xep_loai")

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
            ds_thongbao = ThongBao.objects.filter(user=user)
            context['ds_thongbao'] = ds_thongbao
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
class TC_SCD_Create(CreateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien']
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
            min_date = datetime.date.today()
            context['min_date'] = min_date
            min_time = datetime.datetime.now().time()
            context['min_time'] = min_time
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        ThongBao.objects.create(
            Ngay = datetime.date.today(),
            Gio = datetime.datetime.now().time(),
            TieuDe = 'Giảng viên đặt lịch hẹn',
            NoiDung = f"Cố vấn của bạn đã đặt lịch hẹn với bạn vào ngày {self.object.NgayHen.strftime('%d/%m/%Y')} lúc {self.object.GioHen.strftime('%H:%M')}.",
            TrangThaiTB="Chưa đọc",
            user = self.object.sinhvien.user
        )
        return response

class TC_SCD_Edit(UpdateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien']
    template_name = "lich_hen/lh_edit.html"
    success_url = reverse_lazy('lich_hen')
    context_object_name = 'lichhen'

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            min_date = datetime.date.today()
            context['min_date'] = min_date
            min_time = datetime.datetime.now().time()
            context['min_time'] = min_time
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        ThongBao.objects.create(
            Ngay = datetime.date.today(),
            Gio = datetime.datetime.now().time(),
            TieuDe = 'Giảng viên đặt lịch hẹn',
            NoiDung = f"Cố vấn của bạn đã chỉnh sửa lịch hẹn với bạn vào ngày {self.object.NgayHen.strftime('%d/%m/%Y')} lúc {self.object.GioHen.strftime('%H:%M')}.",
            TrangThaiTB="Chưa đọc",
            user = self.object.sinhvien.user
        )
        return response
    
def comfirm_schedule(request, pk):
    obj = get_object_or_404(LichHen, pk=pk)
    obj.TrangThai = "Đã xác nhận"
    obj.save()
    ThongBao.objects.create(
        Ngay = datetime.date.today(),
        Gio = datetime.datetime.now().time(),
        TieuDe = 'Giảng viên xác nhận lịch hẹn',
        NoiDung = f"Cố vấn của bạn đã xác nhận lịch hẹn với bạn vào ngày {obj.NgayHen.strftime('%d/%m/%Y')} lúc {obj.GioHen.strftime('%H:%M')}.",
        TrangThaiTB="Chưa đọc",
        user = obj.sinhvien.user
    )
    return redirect('lich_hen')

def cancel_schedule(request, pk):
    obj = get_object_or_404(LichHen, pk=pk)
    obj.TrangThai = "Đã hủy"
    obj.save()
    ThongBao.objects.create(
        Ngay = datetime.date.today(),
        Gio = datetime.datetime.now().time(),
        TieuDe = 'Giảng viên hủy lịch hẹn',
        NoiDung = f"Cố vấn của bạn đã hủy lịch hẹn với bạn vào ngày {obj.NgayHen.strftime('%d/%m/%Y')} lúc {obj.GioHen.strftime('%H:%M')}.",
        TrangThaiTB="Chưa đọc",
        user = obj.sinhvien.user
    )
    return redirect('lich_hen')

def meet_schedule(request, pk):
    obj = get_object_or_404(LichHen, pk=pk)
    obj.TrangThai = "Đã gặp"
    obj.save()
    ThongBao.objects.create(
        Ngay = datetime.date.today(),
        Gio = datetime.datetime.now().time(),
        TieuDe = 'Giảng viên xác nhận gặp mặt',
        NoiDung = f"Cố vấn của bạn đã xác nhận bạn có mặt ở lịch hẹn ngày {obj.NgayHen.strftime('%d/%m/%Y')} lúc {obj.GioHen.strftime('%H:%M')}.",
        TrangThaiTB="Chưa đọc",
        user = obj.sinhvien.user
    )
    return redirect('lich_hen')

def absent_schedule(request, pk):
    obj = get_object_or_404(LichHen, pk=pk)
    obj.TrangThai = "Vắng"
    obj.save()
    ThongBao.objects.create(
        Ngay = datetime.date.today(),
        Gio = datetime.datetime.now().time(),
        TieuDe = 'Giảng viên xác nhận vắng mặt',
        NoiDung = f"Cố vấn của bạn đã xác nhận bạn vắng mặt ở lịch hẹn ngày {obj.NgayHen.strftime('%d/%m/%Y')} lúc {obj.GioHen.strftime('%H:%M')}.",
        TrangThaiTB="Chưa đọc",
        user = obj.sinhvien.user
    )
    return redirect('lich_hen')
    


class SinhVien_create(CreateView):
    model = SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'covan', 'lop']
    template_name = "sinh_vien/sv_create.html"
    success_url = reverse_lazy('sinh_vien')

    def get_context_data(self, *args, **kwargs):
        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            covan = CoVan.objects.get(user=user)
            context['covan'] = covan
            context['ds_lop'] = Lop.objects.all()
            curr_year = datetime.datetime.now().year
            context['curr_year'] = curr_year - 18
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
class SinhVien_edit(UpdateView):
    model = SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV', 'covan', 'lop']
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
            curr_year = datetime.datetime.now().year
            context['curr_year'] = curr_year - 18
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
def sinhvien_delete(request, pk):
    obj = get_object_or_404(SinhVien, pk=pk)
    obj.covan = None
    obj.save()
    return redirect("sinh_vien")
    
class Covan_edit(UpdateView):
    model = CoVan
    fields = ['MaCV', 'HoTenCV', 'NgSinhCV', 'SDTCV', 'EmailCV', 'bomon']
    template_name = "co_van/update.html"
    success_url = reverse_lazy('teacher')
    context_object_name = "covan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # Lấy người dùng hiện tại
        covan = CoVan.objects.get(user=user)
        context['covan'] = covan
        context['lops'] = Lop.objects.all()
        context['bomons'] = BoMon.objects.all()    
        curr_year = datetime.datetime.now().year
        context['curr_year'] = curr_year - 25
        return context

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)  # Đăng xuất người dùng
        return redirect('login')