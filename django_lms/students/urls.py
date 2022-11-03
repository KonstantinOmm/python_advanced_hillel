from django.urls import path

from students.views import DeleteStudentView, CreateStudentView
from students.views import DetailStudentView
from students.views import UpdateStudentView
from .views import ListStudentView

# CRUD Create, Read, Update, Delete

app_name = 'students'

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create'),                   # Create
    path('', ListStudentView.as_view(), name='list'),
    path('detail/<int:pk>/', DetailStudentView.as_view(), name='detail'),  # Read
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),  # Delete
]
