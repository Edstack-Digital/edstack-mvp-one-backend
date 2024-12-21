from django.contrib import admin
from .models import Course, User, Tutor

# Register your models here.
admin.site.register(Course)
admin.site.register(Tutor)
admin.site.register(User)