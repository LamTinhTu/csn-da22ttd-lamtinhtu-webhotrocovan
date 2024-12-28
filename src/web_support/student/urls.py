from django.urls import path
from .views import student_view, student_teacher_view, student_xeploai_view, student_lichhen_view, student_detail

urlpatterns = [
 path("", student_view.as_view(), name="student"),
 path("covan", student_teacher_view.as_view(), name = "covan"),
 path("xeploai", student_xeploai_view.as_view(), name = "xeploai"),
 path("lichhen", student_lichhen_view.as_view(), name = "lichhen"),
 path("detail/<str:pk>/", student_detail.as_view(), name="sv_detail")
]