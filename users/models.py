from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUsers(AbstractUser):
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)

    def __str__(self):
        return self.username