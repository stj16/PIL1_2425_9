from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import RegisterSerializer ,UserSerializer
from .models import User 
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]



class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]