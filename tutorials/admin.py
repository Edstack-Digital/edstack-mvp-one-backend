from django.contrib import admin
from .models import Course, User, Video

# Register your models here.
admin.site.register(User)
admin.site.register(Video)
admin.site.register(Course)
