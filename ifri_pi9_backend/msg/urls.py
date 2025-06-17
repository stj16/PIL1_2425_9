from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import msgViewSet # Import msgViewSet, remove others

router = DefaultRouter()
# Register msgViewSet with 'messages' prefix and 'message' basename
router.register(r'messages', msgViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)), # Use include() for router.urls
]
