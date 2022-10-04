from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone_number',
        ]

    def clean(self):
        pass

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_first_name(self):
        return self.cleaned_data['first_name'].title()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].title()

    def clean_phone_number(self):
        value = self.cleaned_data['phone_number']
        return "".join(char for char in value if char in "0123456789-()")
