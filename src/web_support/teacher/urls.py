from django.urls import path
import teacher.views as views
urlpatterns = [
 path("co_van/edit/<str:pk>", views.Covan_edit.as_view(), name="cv_edit"),
 path('', views.teacher_view.as_view(), name="teacher"),
 path("sinh_vien", views.SinhVien_view.as_view(), name = "sinh_vien"),
 path("sinh_vien/create", views.SinhVien_create.as_view(), name="sv_create"),
 path("sinh_vien/edit/<str:pk>", views.SinhVien_edit.as_view(), name="sv_edit"),
 path("sinhvien/delete/<str:pk>", views.sinhvien_delete, name="sv_delete"),
 path("lich_hen", views.LichHen_view.as_view(), name = "lich_hen"),  
 path("lich_hen/create", views.TC_SCD_Create.as_view(), name="cv_lh_create"), 
 path("lichhen/edit/<str:pk>", views.TC_SCD_Edit.as_view(), name="cv_lh_edit"), 
 path("lich_hen/confirm/<str:pk>", views.comfirm_schedule, name="comfirm"),
 path("lich_hen/cancel/<str:pk>", views.cancel_schedule, name="cancel_cv"),
 path("lich_hen/meet/<str:pk>", views.meet_schedule, name="meet"),
 path("lich_hen/absent/<str:pk>", views.absent_schedule, name="absent"),
 path("xep_loai", views.XepLoai_view.as_view(), name = "xep_loai"),
 path("xep_loai/create", views.XepLoai_CreateView.as_view(), name="xl_create"),
 path("xeploai/edit/<int:pk>", views.XepLoai_EditView.as_view(), name="xl_edit"),
 path("xep_loai/delete/<int:pk>", views.xeploai_delete, name="xl_delete"),
 path("logout_cv", views.LogoutView.as_view(), name="logout_cv")
]