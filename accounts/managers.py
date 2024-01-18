from django.contrib.auth.models import BaseUserManager

class Usermanager(BaseUserManager):
    def create_user(self,phone_number,email,full_name,password):
        if not phone_number:
            raise ValueError('شماره تلفن را وارد نکردید')
        if not email:
            raise ValueError('ایمیل را وارد نکردید')
        if not full_name:
            raise ValueError('نام و نام خانوادگی را وارد نکردید')
        user=self.model(phone_number=phone_number,email=self.normalize_email(email),full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,phone_number,email,full_name,password):
        user=self.create_user(phone_number,email,full_name,password)
        user.is_admin=True
        user.save(using=self.db)
        return user
