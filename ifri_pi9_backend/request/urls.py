from django.urls import path
from .views import carrequestList


urlpatterns = [
    path('', carrequestList.as_view(), name='request-list'),
]