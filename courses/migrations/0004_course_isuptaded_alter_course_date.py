# Generated by Django 4.1.3 on 2023-11-04 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_course_slug_alter_categories_id_alter_course_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="isUptaded",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="date",
            field=models.DateField(
                verbose_name=datetime.datetime(2023, 11, 5, 0, 56, 56, 470348)
            ),
        ),
    ]
