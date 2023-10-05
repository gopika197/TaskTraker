from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
