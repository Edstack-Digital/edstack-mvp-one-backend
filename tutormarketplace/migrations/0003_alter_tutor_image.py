# Generated by Django 5.1.4 on 2025-01-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutormarketplace", "0002_remove_tutor_phone_alter_tutor_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutor",
            name="image",
            field=models.URLField(blank=True),
        ),
    ]
