from rest_framework import serializers
from .models import carrequest

class carrequestSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = carrequest
        fields = '__all__'