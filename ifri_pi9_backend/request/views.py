from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import carrequest
from .serializers import carrequestSerializer


# Create your views here.
class carrequestList(generics.ListCreateAPIView):
    queryset = carrequest.objects.all()
    serializer_class = carrequestSerializer
    
