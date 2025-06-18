from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'nom', 'prenom', 'role', 'phone_number', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'nom', 'prenom', 'role', 'phone_number', 'is_active', 'is_staff', 'photo']
        read_only_fields = ['id', 'is_active', 'is_staff']
        