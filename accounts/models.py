from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import Usermanager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    email = models.EmailField(max_length=300, unique=True, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    National_Code=models.CharField(max_length=12, verbose_name='کد ملی', null=True, blank=True)
    Job=models.CharField(max_length=300, verbose_name='شغل', null=True, blank=True)
    Date_of_Birth = models.DateField(verbose_name='تاریخ تولد', null=True, blank=True)
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

    class Meta:
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


class AddressUser(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر',
                             related_name='address_users')
    State = models.CharField(max_length=400, verbose_name='استان', blank=True, null=True)
    City = models.CharField(max_length=400, verbose_name='شهر', blank=True, null=True)
    Neighbourhood = models.CharField(max_length=400, verbose_name='محله', blank=True, null=True)
    Avenue = models.CharField(max_length=400, verbose_name='خیابان', blank=True, null=True)
    Street = models.CharField(max_length=400, verbose_name='کوچه', blank=True, null=True)
    Plaque = models.CharField(max_length=400, verbose_name='پلاک', blank=True, null=True)

    def __str__(self):
        return self.User.phone_number

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'
