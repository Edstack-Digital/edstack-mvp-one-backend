from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    matric = models.CharField(max_length=100)
    university = models.CharField(max_length=400)
    level = models.IntegerField(null = True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Course(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField()

    def __str__(self):
        return self.title


