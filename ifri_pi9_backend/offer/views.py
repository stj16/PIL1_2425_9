from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import caroffer
from .serializers import carofferSerializer


# Create your views here.
class carofferList(generics.ListCreateAPIView):
    queryset = caroffer.objects.all()
    serializer_class = carofferSerializer
    

