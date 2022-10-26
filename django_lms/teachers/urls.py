from django.urls import path

from teachers.views import ListTeacherView, CreateTeacherView, DetailTeacherView, UpdateTeacherView, DeleteTeacherView

app_name = 'teachers'

urlpatterns = [
    path('', ListTeacherView.as_view(), name='list'),
    path('create/', CreateTeacherView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailTeacherView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateTeacherView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTeacherView.as_view(), name='delete'),
]
