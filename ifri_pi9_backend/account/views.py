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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail # For simulation
from django.conf import settings

class RequestPasswordResetView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            # Frontend URL might need to be configurable via settings
            reset_link = f"http://localhost:5173/reset-password/{uidb64}/{token}/"

            # Simulate sending email
            print(f"Password reset link for {user.email}: {reset_link}")

            # In a real scenario, you would send an email here:
            # send_mail(
            #     'Password Reset Request',
            #     f'Please click the following link to reset your password: {reset_link}',
            #     settings.DEFAULT_FROM_EMAIL, # Or your specific sender email
            #     [user.email],
            #     fail_silently=False,
            # )

            return Response({'message': 'If your email is registered, you will receive a password reset link.'}, status=status.HTTP_200_OK)
        else:
            # Still return a generic success message to avoid revealing user existence
            print(f"Password reset attempted for non-existent email: {email}")
            return Response({'message': 'If your email is registered, you will receive a password reset link.'}, status=status.HTTP_200_OK)