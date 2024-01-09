from django.db import models
from job.models import Job

# Create your models here.
class Favorite(models.Model):
    job = models.ForeignKey(
        Job,
        related_name='favorites',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='favorites',
        on_delete=models.CASCADE
    )

class Rating(models.Model):
    value = models.IntegerField()
    job = models.ForeignKey(
        Job,
        related_name='ratings',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'auth.User',
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
        'auth.User',
        related_name='likes',
        on_delete=models.CASCADE
    )
