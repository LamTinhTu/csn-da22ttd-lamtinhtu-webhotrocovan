from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homepage_view(TemplateView):
    template_name = "homepage/homepage.html"

# class login(TemplateView):
class register_view(TemplateView):
    template_name = "login/dangky.html"

# class login(TemplateView):
class login_view(TemplateView):
    template_name = "login/dangnhap.html"   

# class login(TemplateView):
class forgot_view(TemplateView):
    template_name = "login/quenmk.html" 
    
# class login(TemplateView):
class resetpass_view(TemplateView):
    template_name = "login/datlaimk.html"

class datlai_view(TemplateView):
    template_name = "login/datlaimk.html"