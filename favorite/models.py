from django.db import models
from django.contrib.auth import get_user_model
from job.models import Job

User = get_user_model()

# Create your models here.
class Favorite(models.Model):
    favorite_job = models.ForeignKey(
        Job,
        related_name='favorite_job',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='favorite',
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ['user', 'favorite_job']

class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'очень плохо'),
        (2, 'не очень'),
        (3, 'нормально'),
        (4, 'отлично'),
        (5, 'супер')
    )
    value = models.IntegerField(choices=RATING_CHOICES)
    rating_job = models.ForeignKey(
        Job,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='ratings',
        on_delete=models.CASCADE
    )
