from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Job(models.Model):
    title = models.CharField(max_length=50, verbose_name='Вакансия')
    slug = models.SlugField(max_length=50, primary_key=True, blank=True)
    company_title = models.CharField(max_length=20, verbose_name='Название компании')
    company_descr = models.TextField(verbose_name='Описание компании')
    salary = models.CharField(max_length=7, verbose_name='Зарплата')
    who_created = models.ForeignKey(User, related_name='job', on_delete=models.CASCADE,
                                    verbose_name='Представитель компании')
    requirements = models.TextField(verbose_name='Требования')
    experience = models.CharField(max_length=20, verbose_name='Требуемый опыт')
    responsibilities = models.TextField(verbose_name='Обязанности будущего сотрудника')
    working_conditions = models.TextField(verbose_name='Условия')
    applicants = models.ManyToManyField(User, related_name='applicants', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def add_applicant(self, resume):
        self.applicants.add(resume.user)
