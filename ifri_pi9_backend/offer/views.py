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

# carofferList is removed as its functionality is covered by carofferViewSet

class carofferViewSet(viewsets.ModelViewSet):
    queryset = caroffer.objects.all()
    serializer_class = carofferSerializer
    permission_classes = [IsOwnerOrReadOnly] # Kept IsOwnerOrReadOnly, can be adjusted if IsAuthenticated is preferred for creation

    def perform_create(self, serializer):
        """
        Assigns the authenticated user to the car offer upon creation.
        """
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # This case should ideally be prevented by permission_classes,
            # but as a safeguard:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Authentication required to create an offer.")

class MatchingAPIView(APIView):
    def post(self, request):
        depart_address = request.data.get('depart_address')
        arrive_address = request.data.get('arrive_address')
        date_depart_souhaitee_str = request.data.get('date_depart_souhaitee') # YYYY-MM-DD
        heure_depart_souhaitee_str = request.data.get('heure_depart_souhaitee') # HH:MM

        if not all([depart_address, arrive_address, date_depart_souhaitee_str, heure_depart_souhaitee_str]):
            return Response({'error': 'depart_address, arrive_address, date_depart_souhaitee, and heure_depart_souhaitee are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user_depart_lat, user_depart_lng = geocode_address_osm(depart_address)
        if user_depart_lat is None or user_depart_lng is None:
            return Response({'error': f'Could not geocode departure address: {depart_address}'}, status=status.HTTP_400_BAD_REQUEST)

        user_arrive_lat, user_arrive_lng = geocode_address_osm(arrive_address)
        if user_arrive_lat is None or user_arrive_lng is None:
            return Response({'error': f'Could not geocode arrival address: {arrive_address}'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_departure_datetime = datetime.strptime(f"{date_depart_souhaitee_str} {heure_depart_souhaitee_str}", "%Y-%m-%d %H:%M")
        except ValueError:
            return Response({'error': 'Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time.'}, status=status.HTTP_400_BAD_REQUEST)

        results = []
        MAX_DISTANCE_KM = 5  # 5 km
        MAX_TIME_DIFFERENCE_HOURS = 1 # 1 hour

        for offre in caroffer.objects.all():
            # Determine offer's departure point
            offre_start_address_str = offre.start_point_usual if offre.start_point_usual else offre.depart
            if not offre_start_address_str:
                logger.warning(f"Offer {offre.id} has no start_point_usual or depart address, skipping.")
                continue

            offre_depart_lat, offre_depart_lng = geocode_address_osm(offre_start_address_str)
            if offre_depart_lat is None or offre_depart_lng is None:
                logger.warning(f"Could not geocode departure address for offer {offre.id}: {offre_start_address_str}, skipping.")
                continue

            if not offre.arrive: # Assuming 'arrive' is the field name for arrival address in caroffer model
                logger.warning(f"Offer {offre.id} has no arrive address, skipping.")
                continue

            offre_arrive_lat, offre_arrive_lng = geocode_address_osm(offre.arrive)
            if offre_arrive_lat is None or offre_arrive_lng is None:
                logger.warning(f"Could not geocode arrival address for offer {offre.id}: {offre.arrive}, skipping.")
                continue

            # Ensure offre.day and offre.hour are valid
            if offre.day is None or offre.hour is None:
                logger.warning(f"Offer {offre.id} has no day or hour defined, skipping.")
                continue

            try:
                offre_departure_datetime = datetime.combine(offre.day, offre.hour)
            except Exception as e:
                logger.error(f"Error combining date and time for offer {offre.id}: {e}, skipping.")
                continue

            distance_depart = haversine(user_depart_lat, user_depart_lng, offre_depart_lat, offre_depart_lng)
            distance_arrivee = haversine(user_arrive_lat, user_arrive_lng, offre_arrive_lat, offre_arrive_lng)

            if distance_depart < MAX_DISTANCE_KM and distance_arrivee < MAX_DISTANCE_KM:
                time_difference = abs(offre_departure_datetime - user_departure_datetime)
                if (time_difference.total_seconds() / 3600) < MAX_TIME_DIFFERENCE_HOURS:
                    results.append(offre)

        serializer = carofferSerializer(results, many=True)
        return Response(serializer.data)
    

