from .models import msg
from rest_framework import serializers
 
class msgSerializer(serializers.ModelSerializer):
    class Meta:
        model = msg
        fields = '__all__'