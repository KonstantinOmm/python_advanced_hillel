from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from students.forms import CreateStudentForm
from students.models import Student
from students.utils import qs2html

from webargs.djangoparser import use_args
from webargs.fields import Str


# HttpRequest
def index(request):
    return HttpResponse('Welcome to LMS')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    # if 'first_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    # if 'last_name' in args:
    #     students = students.filter(last_name=args['last_name'])

    html_form = """
        <form method="post">
          <label for="fname">First name:</label>
          <input type="text" id="fname" name="first_name" placeholder="John"><br><br>
          <label for="lname">Last name:</label>
          <input type="text" id="lname" name="last_name" placeholder="Doe"><br><br>
          <input type="submit" value="Submit">
        </form> 
    """
    html = qs2html(students)

    # HttpResponse

    response = HttpResponse(html_form + html)
    return response


# @csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f"""
            <form method="post">
                <input type='hidden' name='csrfmiddlewaretoken' value='{token}'>
                <table>
                    {form.as_table()}
                </table>           
              <input type="submit" value="Submit">
            </form> 
        """
    return HttpResponse(html_form)


def update_student(request):
    return None

