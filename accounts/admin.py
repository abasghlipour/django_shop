from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, Otp_code, AddressUser
from django.contrib.auth.models import Group
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Otp_code)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'code', 'created']


@admin.register(AddressUser)
class AddressUserAdmin(admin.ModelAdmin):
    list_display = ['User', 'State', 'City']


class UserAdmin(ModelAdminJalaliMixin, BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'phone_number', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password', 'National_Code', 'Date_of_Birth')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'last_login',)})
    )
    add_fieldsets = (
        (None, {'fields': (
        'phone_number', 'email', 'full_name', 'password1', 'password2', 'National_Code', 'Date_of_Birth')}),
    )
    search_fields = ['email', 'full_name']
    ordering = ['full_name']
    filter_horizontal = []


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
