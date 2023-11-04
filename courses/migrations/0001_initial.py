# Generated by Django 4.1.3 on 2023-11-01 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("imageUrl", models.CharField(max_length=50)),
                (
                    "date",
                    models.DateField(
                        verbose_name=datetime.datetime(2023, 11, 1, 23, 7, 8, 596724)
                    ),
                ),
                ("isActive", models.BooleanField()),
            ],
        ),
    ]