from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# from .models import User
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError


def send_resume_data(email, resume):
    User = get_user_model()
    user = User.objects.get(email=email)
    first_name = user.first_name

    context = {
        'text_detail': f'{first_name}, Ваше резюме было опубликовно на нашем сайте',
        'email': email,
        'domain': 'http://localhost:8000',
        'resume': resume,

    }

    msg_html = render_to_string('resume.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Резюме',
        message,
        'test@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False,
    )

