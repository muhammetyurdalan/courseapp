# Generated by Django 4.1.3 on 2023-11-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0006_course_category_alter_course_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="isActive",
            field=models.BooleanField(default=1),
        ),
    ]