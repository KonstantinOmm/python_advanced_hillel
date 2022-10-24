# from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, ListView

from core.views import CustomUpdateBaseView
from students.forms import CreateStudentForm, StudentFilterForm
from students.forms import UpdateStudentForm
from students.models import Student

# from webargs.djangoparser import use_args
# from webargs.fields import Str


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
# )


    # if len(args) and args.get('first_name') or args.get('last_name'):
    #     students = students.filter(
    #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
    #     )


class ListStudentView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = ''


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/detail.html'


# @csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


# def update_student(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#
#     if request.method == 'GET':
#         form = UpdateStudentForm(instance=student)
#     elif request.method == 'POST':
#         form = UpdateStudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('students:list'))
#
#     return render(request, 'students/update.html', {'form': form})


# class CustomUpdateStudentView(CustomUpdateBaseView):
#     model = Student
#     form_class = UpdateStudentForm
#     success_url = 'students:list'
#     template_name = 'students/update.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'students/delete.html'
    success_url = reverse_lazy('students:list')

