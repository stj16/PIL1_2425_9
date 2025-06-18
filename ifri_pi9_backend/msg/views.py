from rest_framework import viewsets, generics
from .models import msg
from .serializer import msgSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import msg
from django.contrib.auth import get_user_model
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



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_conversations(request):
    user = request.user
    User = get_user_model()
    # Récupère tous les users avec qui il y a eu un échange (envoi ou réception)
    sent_to = msg.objects.filter(sender=user).values_list('receiver', flat=True)
    received_from = msg.objects.filter(receiver=user).values_list('sender', flat=True)
    user_ids = set(list(sent_to) + list(received_from))
    contacts = User.objects.filter(id__in=user_ids)
    data = [
        {
            "id": u.id,
            "name": f"{u.prenom} {u.nom}",
            "avatar": u.photo.url if u.photo else "",
        }
        for u in contacts
    ]
    return Response(data)  

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def conversation_messages(request, user_id):
    user = request.user
    messages = msg.objects.filter(
        (models.Q(sender=user) & models.Q(receiver_id=user_id)) |
        (models.Q(sender_id=user_id) & models.Q(receiver=user))
    ).order_by('timestamp')
    from .serializer import msgSerializer
    return Response(msgSerializer(messages, many=True).data)