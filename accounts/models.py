from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import Usermanager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    email = models.EmailField(max_length=300, unique=True, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین / معمولی')
    trash = models.BooleanField(default=False, verbose_name='حذف شده')

    objects = Usermanager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Otp_code(models.Model):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"

    class Meta:
        verbose_name = 'کد احراز هویت'
        verbose_name_plural = 'کدهای احراز هویت'
