from django.core.mail import send_mail
from django.template.loader import render_to_string
# from .models import User
from django.contrib.auth import get_user_model


def send_recovery_code(email, recovery_code):
    User = get_user_model()

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Обработка случая, когда пользователя нет
        return

    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, кажется, вы забыли пароль или хотите его сменить. Вам отправлен код восстановления:',
        'email': email,
        'domain': 'http://localhost:8000',
        'recovery_code': recovery_code,

    }

    message = render_to_string('text_pass.txt', context)
    
    send_mail(
        'Восстановление пароля',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False,
    )
    print(recovery_code)

