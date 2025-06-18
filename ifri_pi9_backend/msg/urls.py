from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import msgListecreateview, msgDetailview, user_conversations, conversation_messages

router = DefaultRouter()
router.register(r'all', msgListecreateview, basename='msg')

urlpatterns = [
    *router.urls,
    path('<int:pk>/', msgDetailview.as_view(), name='msg-detail'),
    path('conversations/', user_conversations, name='user-conversations'),
    path('messages/<int:user_id>/', conversation_messages, name='conversation-messages'),
]
