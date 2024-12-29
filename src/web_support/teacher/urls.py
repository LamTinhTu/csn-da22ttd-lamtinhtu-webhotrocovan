from django.urls import path
from .views import teacher_view, SinhVien_view, XepLoai_view, LichHen_view, SinhVien_create, Covan_edit, LogoutView, TC_SCD_Create, SinhVien_edit, TC_SCD_Edit

urlpatterns = [
 path('', teacher_view.as_view(), name="teacher"),
 path("sinh_vien", SinhVien_view.as_view(), name = "sinh_vien"),
 path("xep_loai", XepLoai_view.as_view(), name = "xep_loai"),
 path("lich_hen", LichHen_view.as_view(), name = "lich_hen"),
 path("sinh_vien/create", SinhVien_create.as_view(), name="sv_create"),
 path("co_van/edit/<str:pk>", Covan_edit.as_view(), name="cv_edit"),
 path("logout_cv", LogoutView.as_view(), name="logout_cv"),
 path("lichhen/create", TC_SCD_Create.as_view(), name="cv_lh_create"),
 path("sinh_vien/edit/<str:pk>", SinhVien_edit.as_view(), name="sv_edit"),
 path("lichhen/edit", TC_SCD_Edit.as_view(), name="cv_lh_edit")
]