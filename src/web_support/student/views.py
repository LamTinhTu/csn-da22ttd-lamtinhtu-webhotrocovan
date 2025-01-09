from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import SinhVien, sinhvien_xeploai
from teacher.models import CoVan
from schedule.models import LichHen
from message.models import ThongBao
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import random
import datetime

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

class Student_edit(UpdateView):
    model: SinhVien
    fields = ['MaSV', 'HoTenSV', 'NgSinhSV', 'SDTSV', 'EmailSV']
    template_name = "sinhvien/sv_edit.html"
    success_url = reverse_lazy('student')
    context_object_name = 'sinhvien'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # Lấy người dùng hiện tại
        sinhvien = SinhVien.objects.get(user=user)
        covan = sinhvien.covan
        context['covan'] = covan
        lop = sinhvien.lop
        context['lop'] = lop
        curr_year = datetime.datetime.now().year
        context['curr_year'] = curr_year - 18
        return context

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
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user
            sinhvien = SinhVien.objects.get(user=user)
            ds_xeploai = sinhvien.sv_xls.all()
            context['ds_xeploai'] = ds_xeploai
        except CoVan.DoesNotExist:
            return redirect('login')
        return context

class student_lichhen_view(TemplateView):
    template_name = "lichhen/sv_lichhen.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        try:
            sinhvien = SinhVien.objects.get(user=user)
            ds_lichhen = sinhvien.lichhens.all()
            context['ds_lichhen'] = ds_lichhen
            ds_thongbao = ThongBao.objects.filter(user=user)
            context['ds_thongbao'] = ds_thongbao
        except SinhVien.DoesNotExist:
            context['error'] = 'Không tìm thấy sinh viên'
        return context
class ST_SCD_Create(CreateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien']
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
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        ThongBao.objects.create(
            Ngay = datetime.date.today(),
            Gio = datetime.datetime.now().time(),
            TieuDe = 'Sinh viên đăng ký lịch hẹn',
            NoiDung = f"Sinh viên có mã {self.object.sinhvien.MaSV} của bạn đã đặt lịch hẹn với bạn vào ngày {self.object.NgayHen.strftime('%d/%m/%Y')} lúc {self.object.GioHen.strftime('%H:%M')}.",
            TrangThaiTB="Chưa đọc",
            user = self.object.covan.user
        )
        return response
        
    
    
class ST_SCD_Edit(UpdateView):
    model = LichHen
    fields = ['MaH', 'TenBuoiHen', 'NgayHen', 'GioHen', 'DiaDiem', 'TrangThai', 'covan', 'sinhvien']
    template_name = "lichhen/lh_edit.html"
    success_url = reverse_lazy('lichhen')
    context_object_name = 'lichhen'

    def get_context_data(self, *args, **kwargs):        
        try:
            context = super().get_context_data(*args, **kwargs)
            user = self.request.user  # Lấy người dùng hiện tại
            sinhvien = SinhVien.objects.get(user=user)
            context['sinhvien'] = sinhvien
            covan = sinhvien.covan
            context['covan'] = covan
        except CoVan.DoesNotExist:
            return redirect('login')
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        ThongBao.objects.create(
            Ngay = datetime.date.today(),
            Gio = datetime.datetime.now().time(),
            TieuDe = 'Sinh viên chỉnh sửa lịch hẹn',
            NoiDung = f"Sinh viên có mã {self.object.sinhvien.MaSV} của bạn đã chỉnh sửa lịch hẹn với bạn vào ngày {self.object.NgayHen.strftime('%d/%m/%Y')} lúc {self.object.GioHen.strftime('%H:%M')}.",
            TrangThaiTB="Chưa đọc",
            user = self.object.covan.user
        )
        return response
    
def cancel_schdule(request, pk):
    obj = get_object_or_404(LichHen, pk=pk)
    obj.TrangThai = "Yêu cầu hủy"
    obj.save()
    ThongBao.objects.create(
        Ngay = datetime.date.today(),
        Gio = datetime.datetime.now().time(),
        TieuDe = 'Sinh viên hủy lịch hẹn',
        NoiDung = f"Sinh viên có mã số {obj.sinhvien.MaSV} của bạn đã yêu cầu hủy lịch hẹn với bạn vào ngày {obj.NgayHen.strftime('%d/%m/%Y')} lúc {obj.GioHen.strftime('%H:%M')}.",
        TrangThaiTB="Chưa đọc",
        user = obj.covan.user
    )
    return redirect('lichhen')