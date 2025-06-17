from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, userViewSet, RequestPasswordResetView # Added RequestPasswordResetView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', userViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-password-reset/', RequestPasswordResetView.as_view(), name='request_password_reset'), # Added route
    path('', include(router.urls)),
]