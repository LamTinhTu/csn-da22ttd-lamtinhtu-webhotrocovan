from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
# from django.contrib.auth.models import User
from student.models import User

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


class LoginView(TemplateView):
    template_name = "login/dangnhap.html"  

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})  

    def post(self, request, *args, **kwargs):
        tai_khoan = request.POST.get('tai_khoan')
        mat_khau = request.POST.get('mat_khau')

        user = authenticate(request, username=tai_khoan, password=mat_khau)
        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('student') 
            elif user.is_teacher:
                return redirect('teacher')
            else:
                return redirect('login')
        else:
            return self.render_to_response({'error': 'Tên đăng nhập hoặc mật khẩu không chính xác'})
        

