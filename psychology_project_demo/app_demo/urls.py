from django.conf.urls import url
from . import views

urlpatterns = [
    url('UserRegister/', views.UserRegister.as_view()),
    url('UserGetByEmail/<int:pk>/', views.UserGetByEmail.as_view()),
    url('login', views.Login.as_view()),
    url('Forget_password', views.Forget_password.as_view()),
    url('verification_code', views.check_Forget_password_verification_code.as_view()),
    url('resendforgetcode', views.resendforgetcode.as_view()),
    url('setpassword', views.setpassword.as_view()),
]