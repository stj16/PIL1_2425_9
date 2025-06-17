from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from .models import caroffer
from .serializers import carofferSerializer
from .utils import geocode_address_osm, haversine
from .permissions import IsOwnerOrReadOnly
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class carofferList(generics.ListCreateAPIView):
    queryset = caroffer.objects.all()
    serializer_class = carofferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # Ajouter les en-têtes CORS manuellement
        response["Access-Control-Allow-Origin"] = "http://localhost:5173"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        return response

    def create(self, request, *args, **kwargs):
        print("=== NOUVELLE REQUÊTE DE CRÉATION D'OFFRE ===")
        print(f"Utilisateur authentifié: {request.user.is_authenticated}")
        print(f"Données reçues: {request.data}")
        
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            # Récupérer l'utilisateur
            user = request.user
            print(f"Utilisateur: {user.id} - {user.email}")
            
            # Créer une copie mutable des données
            data = request.data.dict() if hasattr(request.data, 'dict') else request.data.copy()
            
            # Ajouter l'utilisateur aux données
            data['user'] = user.id
            
            print(f"Données avant sérialisation: {data}")
            
            # Valider et sauvegarder l'offre
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            
            # Créer l'offre en forçant l'ID utilisateur
            instance = serializer.save(user=user)
            print(f"Offre créée avec succès: {instance.id}")
            
            # Retourner la réponse avec les en-têtes CORS
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            response["Access-Control-Allow-Origin"] = "http://localhost:5173"
            response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response["Access-Control-Allow-Credentials"] = "true"
            return response
            
        except Exception as e:
            print(f"Erreur lors de la création de l'offre: {str(e)}")
            return Response(
                {'error': f"Erreur lors de la création de l'offre", 'details': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        # Cette méthode n'est plus utilisée car nous faisons le save() manuellement dans create()
        # pour avoir plus de contrôle sur la gestion des erreurs
        pass


class carofferViewSet(viewsets.ModelViewSet):
    queryset = caroffer.objects.all()
    serializer_class = carofferSerializer
    permission_classes = [IsOwnerOrReadOnly]



class MatchingAPIView(APIView):
    def post(self, request):
        address = request.data.get('address')
        if not address:
            return Response({'error': 'Adresse requise'}, status=400)
        lat, lng = geocode_address_osm(address)
        if lat is None or lng is None:
            return Response({'error': 'Adresse non trouvée'}, status=400)

        results = []
        for offre in caroffer.objects.all():
            offre_lat, offre_lng = geocode_address_osm(offre.address)
            if offre_lat and offre_lng:
                distance = haversine(lat, lng, offre_lat, offre_lng)
                if distance < 2000:  # 2 km
                    results.append(offre)

        serializer = carofferSerializer(results, many=True)
        return Response(serializer.data)
    

