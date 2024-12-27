from django.db.models.signals import post_save
from django.dispatch import receiver
from tutorials.models import User
from .models import Tutor

# @receiver(post_save, sender=User)
# def create_tutor_profile(sender, instance, created, **kwargs):
#     if created:
#         Tutor.objects.create(user=instance)