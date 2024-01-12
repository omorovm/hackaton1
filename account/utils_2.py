from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from .models import User
from django.contrib.auth import get_user_model


def send_recovery_code(email, recovery_code):
    User = get_user_model()
    user = User.objects.get(email=email)
    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, кажется, вы забыли пароль или хотите его сменить. Вам отправлен код восстановления:',
        'email': email,
        'domain': 'http://localhost:8000',
        'recovery_code': recovery_code,

    }

    msg_html = render_to_string('forgot_pass.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Восстановление пароля',
        message,
        'test@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False,
    )

