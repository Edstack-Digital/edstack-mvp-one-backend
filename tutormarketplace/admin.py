from django.contrib import admin
from .models import Tutor

# Register your models here.
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'courses','badge','rating','image')
    search_fields = ('first_name', 'last_name', 'email', 'courses')
