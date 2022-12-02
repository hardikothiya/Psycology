from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('userregister/', views.UserRegister.as_view()),
    url('userupdate/', views.UserUpdate.as_view()),
    path('getuserbyid/<int:pk>/', views.GetUserById.as_view()),
    url('login', views.Login.as_view()),
    url('forgetpassword_sendcode', views.Forget_password.as_view()),
    url('checkverificationcode', views.check_Forget_password_verification_code.as_view()),
    # url('resendforgetcode', views.resendforgetcode.as_view()),
    # url('setpassword', views.setpassword.as_view()),
    url('validateuser', views.check_user_reg_verification_code.as_view()),
    url('contactus', views.ContactUs.as_view()),
    url('submit_mood', views.Mood.as_view()),
    path('get_mood/<int:pk>', views.Mood1.as_view()),
]