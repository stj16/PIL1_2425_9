from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('email','username', 'nom', 'prenom', 'role', 'password', 'phone_number')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email','username', 'nom', 'prenom', 'role', 'is_active', 'is_staff', 'photo', 'phone_number', 'point_depart_habituel', 'latitude_depart_habituel', 'longitude_depart_habituel', 'horaires_depart_habituel', 'horaires_arrivee_habituel', 'marque_vehicule', 'modele_vehicule', 'couleur_vehicule', 'nombre_places_vehicule']
        