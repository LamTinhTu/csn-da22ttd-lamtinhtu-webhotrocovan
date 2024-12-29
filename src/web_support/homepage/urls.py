from django.urls import path
from .views import homepage_view, register_view, LoginView, forgot_view, datlai_view

urlpatterns = [
 path("", homepage_view.as_view(), name="home"),
 path("register", register_view.as_view(), name="register"),
 path("login", LoginView.as_view(), name="login"),
 path("forgot", forgot_view.as_view(), name="forgot"),
 path("resetpass", datlai_view.as_view(), name="reset")
]

