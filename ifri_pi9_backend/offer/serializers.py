from rest_framework import serializers
from .models import caroffer
 
 
class carofferSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    class Meta:
        model = caroffer
        fields = '__all__'
    
    def get_user(self, obj):
        try:
            if obj.user:
                return f"{obj.user.prenom} {obj.user.nom}"
        except:
            pass
        return "Conducteur"
    
    def get_user_id(self, obj):
        try:
            return obj.user.id if obj.user else None
        except:
            return None
