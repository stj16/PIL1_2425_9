from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import caroffer
from .serializers import carofferSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import caroffer
from .serializers import carofferSerializer
from .utils import geocode_address_osm, haversine
from .permissions import IsOwnerOrReadOnly 


# Create your views here.
class carofferList(generics.ListCreateAPIView):
    queryset = caroffer.objects.all()
    serializer_class = carofferSerializer
    




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
    

