from django.core.management.base import BaseCommand
from accounts.models import Otp_code
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'Remove expired otp code'

    def handle(self, *args, **options):
        expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=3)
        Otp_code.objects.filter(created__lt=expired_time).delete()
        self.stdout.write('all expried otp codes removed')
