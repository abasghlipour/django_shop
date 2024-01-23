from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register'),
    path('otp/',views.OtpCodeView.as_view(),name='otp'),
    path('login/',views.UserRegisterView.as_view(),name='login')
]
