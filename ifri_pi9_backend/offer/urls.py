from django.urls import path
from .views import carofferList


urlpatterns = [
    path('', carofferList.as_view(), name='offer-list'),
]  