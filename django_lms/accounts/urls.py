from django.urls import path

from .views import AccountsRegisterView, AccountLoginView, AccountLogoutView, account_view, AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountsRegisterView.as_view(), name='register'),                    # Create
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_view, name='profile_view'),
    path('update/', AccountUpdateView.as_view(), name='profile_update'),
  ]


