from rest_framework import serializers
from .models import carrequest
 
 
class carrequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrequest
        fields = '__all__'
