import random

from django.contrib import messages
from django.contrib.auth import authenticate, login

from utils import send_mail, send_sms
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, OtpCodeForm, UserLoginForm
from .models import User, Otp_code


# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, template_name=self.template_name, context={'form_register': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_sms(form.cleaned_data['phone_number'], random_code, form.cleaned_data['full_name'])
            Otp_code.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_register_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'کد احراز هویت با موفقیت ارسال شد', 'success')
            return redirect('accounts:otp')
        return render(request, template_name=self.template_name, context={'form_register': form})


class OtpCodeView(View):
    form_class = OtpCodeForm
    template_name = 'accounts/otp.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = Otp_code.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['full_name'],
                                         user_session['password'])
                code_instance.delete()
                del request.session['user_register_info']
                messages.success(request, 'شما با موفقیت ثبت نام شدید', 'success')
                return redirect('home:index')
            else:
                messages.error(request, 'کد شما اشتباه است', 'danger')
                return redirect('accounts:otp')
        return redirect('home:index')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next')
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:index')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, template_name=self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'شما با موفقیت وارد شدید', 'success')
                if self.next:
                    return redirect(self.next)
