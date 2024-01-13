from django.core.mail import send_mail
from django.template.loader import render_to_string
# from .models import User
from django.contrib.auth import get_user_model


def send_activation_code(email, activation_code):
    User = get_user_model()

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Обработка случая, когда пользователя нет
        return

    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, спасибо за регистрацию на нашем сайте!',
        'email': email,
        'domain': 'http://localhost:8000',
        'activation_code': activation_code,
    }

    # render_to_string для формирования текстового сообщения
    message = render_to_string('text_email.txt', context)

    send_mail(
        'Активация аккаунта',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False,
    )
