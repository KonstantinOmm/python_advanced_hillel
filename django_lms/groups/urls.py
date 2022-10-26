from django.urls import path

from .views import UpdateGroupView
from .views import ListGroupView
from .views import DeleteGroupView
from .views import DetailGroupView
from .views import CreatGroupView

app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreatGroupView.as_view(), name='create'),
    path('detail/<int:pk>/', DetailGroupView.as_view(), name='detail'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteGroupView.as_view(), name='delete'),
]