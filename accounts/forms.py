from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Otp_code


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('رمز عبور یکی نیست')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = (ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\">this form</a>"))

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name', 'password', 'last_login']


class UserRegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='تایید رمز عبور',
                                widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور'}))

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'email', 'password']
        labels = {'password': 'رمز عبور'}
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'شماره تلفن'}),
            'email': forms.TextInput(attrs={'placeholder': 'ایمیل'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
            raise ValidationError('رمز عبور با تکرار آن برابر نیست')
        return cd['password2']


class OtpCodeForm(forms.ModelForm):
    class Meta:
        model = Otp_code
        fields = ['code', ]
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'کد احراز هویت',})
        }


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11, label='شماره تلفن',
                                   widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن','onclick':"togglePasswordVisibility()"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}))

