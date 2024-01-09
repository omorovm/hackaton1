from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=50, decimal_places=2, validators=[MinValueValidator(0),], blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job')