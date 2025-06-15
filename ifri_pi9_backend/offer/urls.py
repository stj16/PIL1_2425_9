from django.urls import path
from .views import carofferList
from .views import carofferList, MatchingAPIView


urlpatterns = [
    path('', carofferList.as_view(), name='offer-list'),
    path('matching/', MatchingAPIView.as_view(), name='offer-matching'),
]