from django.db import models

# Create your models here.
class Tutor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    courses = models.CharField(max_length=400)
    badge = models.BooleanField()
    rating = models.CharField(max_length=10, choices=[('1','1'),('2','2',),('3','3'),('4','4'),('5','5')])
    image = models.URLField(blank = True)

    def __str__(self):
        return f"Tutor: {self.email}"
