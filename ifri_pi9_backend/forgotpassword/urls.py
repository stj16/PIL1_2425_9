from django.urls import path
from .views import ResetPasswordView


urlpatterns = [
    path('', ResetPasswordView.as_view(), name='reset-password-list'),
]  