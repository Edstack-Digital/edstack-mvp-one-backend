# Generated by Django 5.1.4 on 2025-02-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0005_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
