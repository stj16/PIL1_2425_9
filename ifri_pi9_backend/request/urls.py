from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import carrequestViewSet, FindOffersForRequestView # Import FindOffersForRequestView

router = DefaultRouter()
router.register(r'requests', carrequestViewSet, basename='request')

urlpatterns = [
    path('', include(router.urls)),
    path('requests/<int:request_id>/find_offers/', FindOffersForRequestView.as_view(), name='find_offers_for_request'),
]