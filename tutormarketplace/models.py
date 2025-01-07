from django.db import models
from tutorials.models import User

# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    courses = models.CharField(max_length=400)
    badge = models.BooleanField()
    rating = models.CharField(max_length=10, choices=[('1','1'),('2','2',),('3','3'),('4','4'),('5','5')])
    image = models.URLField(blank = True)

    def __str__(self):
        return f"Tutor: {self.user.email}"