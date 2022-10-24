from django.urls import path

from students.views import create_student
from students.views import DeleteStudentView
from students.views import DetailStudentView
from students.views import ListStudentView
# from students.views import update_student
# from students.views import CustomUpdateStudentView
from students.views import UpdateStudentView

# CRUD Create, Read, Update, Delete

app_name = 'students'

urlpatterns = [
    path('create/', create_student, name='create'),                    # Create
    path('', ListStudentView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),  # Read
    # path('update/<int:student_id>/', update_student, name='update'),   # Update
    # path('update/<int:pk>/', CustomUpdateStudentView.update, name='update'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),  # Delete
]
