# Generated by Django 4.1.3 on 2023-11-04 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(auto_created=True,primary_key=True, serialize=False,verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2023, 11, 4, 14, 1, 4, 750010)),
        ),
    ]
