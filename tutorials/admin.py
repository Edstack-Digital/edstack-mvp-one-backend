from django.contrib import admin
from .models import Course, User, Tutor

# Register your models here.
admin.register(Course)
admin.register(Tutor)
admin.register(User)