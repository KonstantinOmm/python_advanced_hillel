# Generated by Django 4.1.1 on 2022-10-21 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_teachers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='heandman',
            new_name='headman',
        ),
    ]
