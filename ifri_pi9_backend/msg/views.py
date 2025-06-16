from rest_framework import viewsets, generics
from .models import msg
from .serializer import msgSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class msgListecreateview(viewsets.ModelViewSet):
    queryset = msg.objects.all()
    serializer_class = msgSerializer

class msgDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = msg.objects.all()
    serializer_class = msgSerializer




class msgViewSet(viewsets.ModelViewSet):
    queryset = msg.objects.all()
    serializer_class = msgSerializer
    permission_classes = [IsOwnerOrReadOnly]