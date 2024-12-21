from django.urls import path
from .views import teacher_view, SinhVien_view, XepLoai_view, LichHen_view

urlpatterns = [
 path('', teacher_view.as_view(), name="teacher"),
 path("sinh_vien", SinhVien_view.as_view(), name = "sinh_vien"),
 path("xep_loai", XepLoai_view.as_view(), name = "xep_loai"),
 path("lich_hen", LichHen_view.as_view(), name = "lich_hen")
]