from django.db import models
from django.contrib.auth import get_user_model
from job.models import Job


User = get_user_model()


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume')
    specializations = [
        ('Front-end разработка', 'Front-end разработка'),
        ('Back-end разработка', 'Back-end разработка'),
        ('Мобильная разработка', 'Мобильная разработка'),
        ('Data science', 'Data science'),
        ('UX/UI дизайн', 'UX/UI дизайн')
    ]
    specialization = models.CharField(max_length=45, choices=specializations)
    sex_choice = [
        ('f', 'female'),
        ('m', 'male')
    ]
    sex = models.CharField(max_length=1, choices=sex_choice)
    city_of_residence = models.CharField(max_length=50, verbose_name='Город проживания')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона')
    citizenship = models.CharField(max_length=30)
    profile_photo = models.ImageField(width_field=354, height_field=472, upload_to='profile', blank=True)
    skills = models.TextField(verbose_name='Навыки, скиллы')
    cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    education_choice = [
        ('Среднее', 'Среднее'),
        ('Среднее специальное', 'Среднее специальное'),
        ('Неоконченное высшее', 'Неоконченное высшее'),
        ('Высшее', 'Высшее'),
        ('Бакалавр', 'Бакалавр'),
        ('Магистр', 'Магистр'),
        ('Кандидат наук', 'Кандидат наук'),
        ('Доктор наук', 'Доктор наук'),
    ]
    education = models.CharField(max_length=20, choices=education_choice, verbose_name='Уровень образования')
    expected_salary = models.CharField(max_length=5, blank=True)
    applied_vacancies = models.ManyToManyField(Job, related_name='applicants_resumes', blank=True)
    statuses = [
        ('viewed', 'Просмотрено'),
        ('rejected', 'Отказано'),
        ('contact_soon', 'Кандидатура подходит, скоро свяжемся'),
    ]
    status = models.CharField(max_length=20, choices=statuses, blank=True, null=True)


    def __str__(self):
        return f'{self.id} - resume of: {self.user}'