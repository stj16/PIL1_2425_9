from django.db import models
from django.conf import settings

# Create your models here.
class caroffer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    depart = models.CharField(max_length=200)
    arrive = models.CharField(max_length=200)
    start_point_usual = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    day = models.DateField(auto_now_add=True)
    hour = models.TimeField(auto_now_add=True)
    place = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        ordering = ['-date_time']
        
    def __str__(self):
        return f"{self.user.username} - {self.depart} vers {self.arrive}"
    
    