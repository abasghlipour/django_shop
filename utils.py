from ippanel import Client
from django.core.mail import send_mail


def send_sms(phone_number, otp_code, full_name):
    api_key = "rDQJQVV_wI1tP5QPc1BN4u8vYdcaTQM2GuSfKUeoqpw="
    sms = Client(api_key)
    message = sms.send(
        sender="+983000505",
        recipients=[phone_number, ],
        message=f' خوش امدید:کد تایید شما {otp_code} \nعباس پروژه',
        summary='description'
    )


def send_email(email, subject, message):
    from_email = 'info@abas-project.ir'
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[email, ], fail_silently=False)
