# Generated by Django 4.1.1 on 2022-09-29 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]