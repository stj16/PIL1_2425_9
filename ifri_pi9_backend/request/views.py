from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import carrequest
from .serializers import carrequestSerializer
from .permissions import IsOwnerOrReadOnly 

# Create your views here.
class carrequestList(generics.ListCreateAPIView):
    queryset = carrequest.objects.all()
    serializer_class = carrequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class carrequestViewSet(viewsets.ModelViewSet):
    queryset = carrequest.objects.all()
    serializer_class = carrequestSerializer
    permission_classes = [IsOwnerOrReadOnly]