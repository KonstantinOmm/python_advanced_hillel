from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, ListView, CreateView

from students.forms import CreateStudentForm, StudentFilterForm
from students.forms import UpdateStudentForm
from students.models import Student


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        students = Student.objects.select_related('group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form


class DetailStudentView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/detail.html'


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'students/create.html'
    form_class = CreateStudentForm
    success_url = reverse_lazy('students:list')


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')

