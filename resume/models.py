from django.db import models
from account.models import User

class Resume(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='resume'
    )
