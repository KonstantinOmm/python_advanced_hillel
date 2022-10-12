# Generated by Django 4.1.1 on 2022-10-06 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" value less than two symbols')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(error_messages={'min_length': '"last_name" value less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
