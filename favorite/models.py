from django.db import models
from account.models import User
from job.models import Job

# Create your models here.
class Favorite(models.Model):
    job = models.ForeignKey(
        Job,
        related_name='favorites',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        related_name='favorites',
        on_delete=models.CASCADE
    )

class Rating(models.Model):
    RATING_CHOICES = (
        (1, 'очень плохо'),
        (2, 'не очень'),
        (3, 'нормально'),
        (4, 'отлично'),
        (5, 'супер')
    )
    value = models.IntegerField(choices=RATING_CHOICES)
    job = models.ForeignKey(
        Job,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        related_name='ratings',
        on_delete=models.CASCADE
    )

class Like(models.Model):
    job = models.ForeignKey(
        Job,
        related_name='likes',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        related_name='likes',
        on_delete=models.CASCADE
    )
