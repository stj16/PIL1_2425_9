from rest_framework import viewsets, generics
from .models import msg
from .serializer import msgSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated # Import IsAuthenticated

# Create your views here.
# msgListecreateview and msgDetailview are removed as their functionality
# is covered by msgViewSet and the router.

class msgViewSet(viewsets.ModelViewSet):
    queryset = msg.objects.all()
    serializer_class = msgSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # Added IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)