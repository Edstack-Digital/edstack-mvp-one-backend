from django.apps import AppConfig


class TutormarketplaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tutormarketplace"

# def ready(self):
#     import tutormarketplace.signals