from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


def send_about_resume(email):
    User = get_user_model()
    user = User.objects.get(email=email)
    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, на вашу вакансию пришел отклик! Скорее проверьте кандидатуру и дайте обратную связь',
        'email': email,
        'domain': 'http://localhost:8000',

    }

    message = render_to_string('text_respond.txt', context)
    
    send_mail(
        'Пришел отклик на вакансию',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False,
    )

