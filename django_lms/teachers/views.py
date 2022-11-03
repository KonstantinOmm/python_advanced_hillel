from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt    # noqa
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView, ListView


from teachers.forms import UpdateTeacherForm, CreateTeacherForm, TeacherFilterForm


from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'

    def get_queryset(self):
        teachers = Teacher.objects.all()
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teachers)

        return filter_form


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')
    form_class = CreateTeacherForm


class DetailTeacherView(LoginRequiredMixin, DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/update.html'
    success_url = reverse_lazy('teachers:list')
    form_class = UpdateTeacherForm


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
