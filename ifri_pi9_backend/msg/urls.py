from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import msgListecreateview, msgDetailview

router = DefaultRouter()
router.register(r'', msgListecreateview, basename='msg')

urlpatterns = [
    *router.urls,
    path('<int:pk>/', msgDetailview.as_view(), name='msg-detail'),
]
