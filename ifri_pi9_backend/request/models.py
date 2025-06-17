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
        related_name='car_requests'
    )
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
    
    
class Meta:
        ordering = ['-created_at']
        verbose_name = "Demande de covoiturage"
        verbose_name_plural = "Demandes de covoiturage"

def __str__(self):
    return f"Demande de {self.user} : {self.depart} → {self.arrive} le {self.date}"
      
    
    