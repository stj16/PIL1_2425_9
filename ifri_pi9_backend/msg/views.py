from rest_framework import viewsets, generics
from .models import msg
from .serializer import msgSerializer

# Create your views here.
class msgListecreateview(viewsets.ModelViewSet):
    queryset = msg.objects.all()
    serializer_class = msgSerializer

class msgDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = msg.objects.all()
    serializer_class = msgSerializer

