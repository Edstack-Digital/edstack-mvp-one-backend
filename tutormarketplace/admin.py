from django.contrib import admin
from .models import Tutor

# Register your models here.
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('user', 'courses','badge','rating','image')
    search_fields = ('user__email', 'courses')
