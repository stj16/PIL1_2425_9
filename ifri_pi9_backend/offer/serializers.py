from rest_framework import serializers
from .models import caroffer
 
 
class carofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = caroffer
        fields = '__all__'
