# Generated by Django 4.1.3 on 2023-11-06 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0007_alter_course_date_alter_course_isactive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="selectedCourses",
                to="courses.categories",
            ),
        ),
    ]
