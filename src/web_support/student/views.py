from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class student_view(TemplateView):
    template_name = "sinhvien/sv_Sinhvien.html"

class student_teacher_view(TemplateView):
    template_name = "covan/sv_covan.html"

class student_xeploai_view(TemplateView):
    template_name = "xeploai/sv_xeploai.html"

class student_lichhen_view(TemplateView):
    template_name = "lichhen/sv_lichhen.html"
