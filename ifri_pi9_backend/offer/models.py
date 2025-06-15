from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class caroffer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    depart = models.CharField(max_length=200)
    arrive = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    date_time = models.DateTimeField(auto_now_add=True)
    place = models.IntegerField()
    price = models.IntegerField()
    
    