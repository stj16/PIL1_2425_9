from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator
from account.models import User

# Create your models here.


class caroffer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Utilisateur"
    )
    depart = models.CharField(max_length=200, verbose_name="Ville de départ")
    arrive = models.CharField(max_length=200, verbose_name="Ville d'arrivée")
    matricule = models.CharField(max_length=200, verbose_name="Immatriculation")
    day = models.DateField(verbose_name="Jour du trajet")
    hour = models.TimeField(verbose_name="Heure du trajet")
    start_point_usual = models.CharField(max_length=200, verbose_name="Point de départ précis")
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    place = models.PositiveIntegerField(
        verbose_name="Nombre de places",
        validators=[MinValueValidator(1)]
    )
    price = models.PositiveIntegerField(
        verbose_name="Prix (FCFA)",
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"Trajet {self.depart} → {self.arrive} - {self.day} à {self.hour}"

    class Meta:
        verbose_name = "Offre de covoiturage"
        verbose_name_plural = "Offres de covoiturage"
        ordering = ['-date_time']
    
    
