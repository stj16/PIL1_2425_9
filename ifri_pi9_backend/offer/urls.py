from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchingAPIView, carofferViewSet # Removed carofferList, added carofferViewSet

router = DefaultRouter()
router.register(r'offers', carofferViewSet, basename='offer')

urlpatterns = [
    path('matching/', MatchingAPIView.as_view(), name='offer-matching'),
    path('', include(router.urls)), # This will handle '/offers/', '/offers/<pk>/', etc.
]