from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Это поле обязательно для заполнения!')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)
    is_employer = models.BooleanField(default=False)
    employer_activation_code = models.CharField(max_length=10, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.id} - {self.email}'

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='0123456789')
        self.activation_code = code

    def create_employer_activation_code(self):
        employer_code = get_random_string(length=10, allowed_chars='0123456789')
        self.employer_activation_code = employer_code


