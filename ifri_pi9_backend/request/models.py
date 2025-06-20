from django.db import models
from django.conf import settings

# Create your models here.
class carrequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    depart = models.CharField(max_length=200)
    arrive = models.CharField(max_length=200)
    start_hours_usual = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)