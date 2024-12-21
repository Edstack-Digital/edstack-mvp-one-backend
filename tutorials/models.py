from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    matric = models.CharField(max_length=100)
    university = models.CharField(max_length=400)
    level = models.IntegerField()

class Tutor(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    courses = models.CharField(max_length=400)
    badge = models.BooleanField()
    rating = models.IntegerField()
    phone = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField()

    def __str__(self):
        return self.title


