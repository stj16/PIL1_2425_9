from django.urls import path
from .views import RegisterView, UserProfileView, list_users
from rest_framework_simplejwt.views import (
 TokenObtainPairView,
  TokenRefreshView,
  )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserProfileView.as_view(), name='user-profile'),
    path('users/', list_users, name='list-users'),
]
