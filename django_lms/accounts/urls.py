from django.urls import path

from .views import AccountsRegisterView, AccountLoginView, AccountLogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountsRegisterView.as_view(), name='register'),                    # Create
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
  ]


