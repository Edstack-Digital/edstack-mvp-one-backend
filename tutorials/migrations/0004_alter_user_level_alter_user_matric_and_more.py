# Generated by Django 5.1.4 on 2025-01-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutorials", "0003_delete_tutor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="level",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="matric",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="university",
            field=models.CharField(blank=True, max_length=400),
        ),
    ]