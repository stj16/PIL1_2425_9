from rest_framework import viewsets, generics
from .serializers import RegisterSerializer, UserSerializer
from .models import User 
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.exclude(id=request.user.id)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]