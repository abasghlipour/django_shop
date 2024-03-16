from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('otp/', views.OtpCodeView.as_view(), name='otp'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('resend/', views.ResendOtpCodeView.as_view(), name='resend'),
    path('reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset/done/', views.ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset/confirm/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('profile/', views.UserProfileView.as_view(), name='profile')
]
