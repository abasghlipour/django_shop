# Generated by Django 5.0.1 on 2024-03-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Date_of_Birth',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تولد'),
        ),
        migrations.AddField(
            model_name='user',
            name='Job',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='شغل'),
        ),
        migrations.AddField(
            model_name='user',
            name='National_Code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='کد ملی'),
        ),
    ]
