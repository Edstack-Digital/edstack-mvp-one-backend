from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    firstname = models.CharField()
    lastname = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
    matric = models.CharField()
    university = models.CharField()
    level = models.IntegerField()

class Tutor(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    courses = models.CharField()
    badge = models.CharField()
    rating = models.IntegerField()
    phone = models.CharField()
    image = models.URLField()

class Course(models.Model):
    name = models.CharField()
    url = models.URLField()


