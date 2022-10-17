from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from core.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        # verbose_name='group name',
        # db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field less than two symbols')]
    )
    group_start_date = models.DateField(default=date.today, null=True, blank=True, validators=[validate_start_date])
    group_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'groups'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            group_name = f.group_name()
            group_start_date = f.date()
            group_description = f.description()
            st = cls(group_name=group_name, group_start_date=group_start_date, group_description=group_description)
            try:
                st.full_clean()
                st.save()
            except ValidationError:
                print('Incorrect data')
