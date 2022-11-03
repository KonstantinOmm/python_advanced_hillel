# Generated by Django 4.1.1 on 2022-10-20 15:50

import core.validators
import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('group_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"group_name" field less than two symbols')])),
                ('group_start_date', models.DateField(blank=True, default=datetime.date.today, null=True, validators=[core.validators.validate_start_date])),
                ('group_description', models.TextField(max_length=1000)),
                ('group_end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
