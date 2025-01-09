from django.urls import path
import student.views as views
urlpatterns = [
 path("", views.student_view.as_view(), name="student"),
 path("covan", views.student_teacher_view.as_view(), name = "covan"),
 path("xeploai", views.student_xeploai_view.as_view(), name = "xeploai"),
 path("lichhen", views.student_lichhen_view.as_view(), name = "lichhen"),
 path("logout_sv", views.LogoutView.as_view(), name="logout_sv"),
 path("lichhen/create", views.ST_SCD_Create.as_view(), name="sv_lh_create"),
 path("edit/<str:pk>", views.Student_edit.as_view(), name="sv_edit_self"),
 path("lichhen/edit/<str:pk>", views.ST_SCD_Edit.as_view(), name="sv_lh_edit"),
 path("lichhen/cancel/<str:pk>", views.cancel_schdule, name="cancel_sv")
]