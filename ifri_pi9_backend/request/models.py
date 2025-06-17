from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings 

# Create your models here.
class carrequest(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur",
        related_name='car_requests',
        null=True, blank=True # Temporarily re-adding null=True, blank=True AGAIN
    )
    depart = models.CharField(max_length=255, verbose_name="Point de départ souhaité") # default="" removed
    arrive = models.CharField(max_length=255, verbose_name="Point d'arrivée souhaité") # default="" removed
    latitude_depart = models.FloatField(blank=True, null=True, verbose_name="Latitude départ")
    longitude_depart = models.FloatField(blank=True, null=True, verbose_name="Longitude départ")
    latitude_arrivee = models.FloatField(blank=True, null=True, verbose_name="Latitude arrivée")
    longitude_arrivee = models.FloatField(blank=True, null=True, verbose_name="Longitude arrivée")

    date = models.DateField(
        verbose_name="Date du trajet",
        default=timezone.now  # Utilise la date actuelle comme valeur par défaut
    )
    
    hour = models.TimeField(
        verbose_name="Heure de départ",
        default=timezone.now  # Utilise l'heure actuelle comme valeur par défaut
    )
    
    place = models.PositiveIntegerField(
        verbose_name="Nombre de places",
        default=1  # Valeur par défaut de 1 place
    )
    
    commentaire = models.TextField(
        blank=True, 
        verbose_name="Commentaire",
        default=""  # Chaîne vide comme valeur par défaut
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création") # default removed, auto_now_add restored

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Demande de covoiturage"
        verbose_name_plural = "Demandes de covoiturage"

    def __str__(self):
        return f"Demande de {self.user.email if self.user else 'Utilisateur inconnu'} : {self.depart} → {self.arrive} le {self.date} à {self.hour}"