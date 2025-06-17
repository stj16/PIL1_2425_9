import logging
from rest_framework import serializers
from .models import caroffer

logger = logging.getLogger(__name__)

class carofferSerializer(serializers.ModelSerializer):
    class Meta:
        model = caroffer
        fields = '__all__'
        read_only_fields = ('user', 'date_time')
    
    def validate(self, attrs):
        # Vérifier que les champs requis sont présents
        required_fields = ['depart', 'arrive', 'day', 'hour', 'start_point_usual', 'place', 'price']
        for field in required_fields:
            if field not in attrs or not attrs[field]:
                raise serializers.ValidationError({field: 'Ce champ est obligatoire'})
        
        # Convertir day et hour en chaînes si ce n'est pas déjà le cas
        if 'day' in attrs and not isinstance(attrs['day'], str):
            attrs['day'] = str(attrs['day'])
            
        if 'hour' in attrs and not isinstance(attrs['hour'], str):
            attrs['hour'] = str(attrs['hour'])
        
        return attrs
