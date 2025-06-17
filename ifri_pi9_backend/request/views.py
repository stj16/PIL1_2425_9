from django.shortcuts import render
from rest_framework import viewsets ,generics
from .models import carrequest
from .serializers import carrequestSerializer
from .permissions import IsOwnerOrReadOnly 
from rest_framework.permissions import IsAuthenticated # Import IsAuthenticated

# Create your views here.
# Remove carrequestList as its functionality is covered by carrequestViewSet

class carrequestViewSet(viewsets.ModelViewSet):
    queryset = carrequest.objects.all()
    serializer_class = carrequestSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # Added IsAuthenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# IsAuthenticated is already imported
from offer.models import caroffer # Adjusted import path
from offer.serializers import carofferSerializer # Adjusted import path
from offer.utils import geocode_address_osm, haversine # Adjusted import path
from datetime import datetime, time
import logging

logger = logging.getLogger(__name__)

class FindOffersForRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, request_id):
        try:
            specific_request = carrequest.objects.get(pk=request_id)
        except carrequest.DoesNotExist:
            return Response({'error': 'Demande non trouvée'}, status=status.HTTP_404_NOT_FOUND)

        request_depart_lat, request_depart_lng = specific_request.latitude_depart, specific_request.longitude_depart
        request_arrive_lat, request_arrive_lng = specific_request.latitude_arrivee, specific_request.longitude_arrivee

        if not all([request_depart_lat, request_depart_lng, request_arrive_lat, request_arrive_lng]):
            logger.warning(f"La demande {request_id} n'a pas de coordonnées de départ/arrivée complètes. Tentative de géocodage...")
            if specific_request.depart and not (request_depart_lat and request_depart_lng):
                lat, lng = geocode_address_osm(specific_request.depart)
                if lat is not None and lng is not None:
                    specific_request.latitude_depart, specific_request.longitude_depart = lat, lng
                    request_depart_lat, request_depart_lng = lat, lng
                else:
                    logger.error(f"Échec du géocodage de l'adresse de départ pour la demande {request_id}: {specific_request.depart}")

            if specific_request.arrive and not (request_arrive_lat and request_arrive_lng):
                lat, lng = geocode_address_osm(specific_request.arrive)
                if lat is not None and lng is not None:
                    specific_request.latitude_arrivee, specific_request.longitude_arrivee = lat, lng
                    request_arrive_lat, request_arrive_lng = lat, lng
                else:
                    logger.error(f"Échec du géocodage de l'adresse d'arrivée pour la demande {request_id}: {specific_request.arrive}")

            # Save the request if coordinates were updated by geocoding
            # This assumes you want to persist successfully geocoded coordinates back to the model instance
            # specific_request.save() # Consider if this save is appropriate here or should be handled elsewhere

            if not all([request_depart_lat, request_depart_lng, request_arrive_lat, request_arrive_lng]):
                return Response({'error': 'Coordonnées de départ/arrivée manquantes ou invalides pour la demande après tentative de géocodage.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            request_departure_datetime = datetime.combine(specific_request.date, specific_request.hour)
        except TypeError: # Handles if date or hour is None
             logger.error(f"Date ou heure manquante pour la demande {request_id}.")
             return Response({'error': 'Date ou heure de départ invalide pour la demande.'}, status=status.HTTP_400_BAD_REQUEST)


        matching_offers = []
        MAX_DISTANCE_KM = 5
        MAX_TIME_DIFFERENCE_HOURS = 1

        for offre in caroffer.objects.all():
            offre_start_address = offre.start_point_usual or offre.depart
            if not offre_start_address or not offre.arrive:
                logger.debug(f"Offre {offre.id} sautée: adresse de départ ou d'arrivée manquante.")
                continue

            offre_depart_lat, offre_depart_lng = geocode_address_osm(offre_start_address)
            offre_arrive_lat, offre_arrive_lng = geocode_address_osm(offre.arrive)

            if not all([offre_depart_lat, offre_depart_lng, offre_arrive_lat, offre_arrive_lng]):
                logger.debug(f"Offre {offre.id} sautée: échec du géocodage pour l'adresse de départ ou d'arrivée.")
                continue

            if offre.day is None or offre.hour is None:
                logger.debug(f"Offre {offre.id} sautée: jour ou heure de départ manquant.")
                continue

            try:
                offre_departure_datetime = datetime.combine(offre.day, offre.hour)
            except TypeError: # Handles if day or hour is None (already checked but good for safety)
                logger.error(f"Erreur de combinaison date/heure pour l'offre {offre.id}.")
                continue


            distance_depart = haversine(request_depart_lat, request_depart_lng, offre_depart_lat, offre_depart_lng)
            distance_arrivee = haversine(request_arrive_lat, request_arrive_lng, offre_arrive_lat, offre_arrive_lng)

            if distance_depart < MAX_DISTANCE_KM and distance_arrivee < MAX_DISTANCE_KM:
                time_difference = abs(offre_departure_datetime - request_departure_datetime)
                if (time_difference.total_seconds() / 3600) < MAX_TIME_DIFFERENCE_HOURS:
                    matching_offers.append(offre)

        serializer = carofferSerializer(matching_offers, many=True)
        return Response(serializer.data)