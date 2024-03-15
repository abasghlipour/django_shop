import requests
from django.core.mail import send_mail


def send_sms(phone_number, otp_code, full_name):
    api_key = "rDQJQVV_wI1tP5QPc1BN4u8vYdcaTQM2GuSfKUeoqpw="
    requests.get(
        f'http://ippanel.com:8080/?apikey={api_key}&pid=7uvx79ioelosoty&fnum=3000505&tnum={phone_number}&p1=verification-code&v1={otp_code}'
    )


def send_email(email, subject, message):
    from_email = 'info@abas-project.ir'
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[email, ], fail_silently=False)
