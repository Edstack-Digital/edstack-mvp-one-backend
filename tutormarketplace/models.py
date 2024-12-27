from django.db import models
from tutorials.models import User

# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor_profile')
    courses = models.CharField(max_length=400)
    badge = models.BooleanField()
    rating = models.IntegerField()
    phone = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return f"Tutor: {self.user.email}"