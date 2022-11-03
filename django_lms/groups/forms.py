from django import forms
from django_filters import FilterSet

from students.models import Student
from .models import Group


class GroupBaseForm(forms.ModelForm):
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'}),
            'group_end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CreateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'] = forms.ModelMultipleChoiceField(
            queryset=Student.objects.select_related('group'),
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'headman'
        ]


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(student.pk, f'{student.first_name} {student.last_name}') for student in self.instance.students.all()],
            label='Headman',
            required=False,
        )
        self.fields['headman_field'].choices.insert(0, (0, '------'))

    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_date',
            'headman',
        ]


class GroupFilterForm(FilterSet):
    class Meta:
        model = Group
        fields = {
            'group_name': ['exact', 'icontains'],
        }
