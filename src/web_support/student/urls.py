from django.urls import path
from .views import student_view, student_teacher_view, student_xeploai_view, student_lichhen_view, student_detail, LogoutView, ST_SCD_Create, Student_edit, ST_SCD_Edit

urlpatterns = [
 path("", student_view.as_view(), name="student"),
 path("covan", student_teacher_view.as_view(), name = "covan"),
 path("xeploai", student_xeploai_view.as_view(), name = "xeploai"),
 path("lichhen", student_lichhen_view.as_view(), name = "lichhen"),
 path("logout_sv", LogoutView.as_view(), name="logout_sv"),
 path("lichhen/create", ST_SCD_Create.as_view(), name="sv_lh_create"),
 path("edit", Student_edit.as_view(), name="sv_edit_self"),
 path("lichhen/edit", ST_SCD_Edit.as_view(), name="sv_lh_edit")
]