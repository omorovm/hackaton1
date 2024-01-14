from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


def send_employer_activation_code(email, employer_activation_code):
    User = get_user_model()
    user = User.objects.get(email=email)
    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, ваш запрос принят!',
        'email': email,
        'domain': 'http://localhost:8000',
        'employer_activation_code': employer_activation_code,

    }

    message = render_to_string('text_emp.txt', context)
    send_mail(
        'Разместить вакансию',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False,
    )

