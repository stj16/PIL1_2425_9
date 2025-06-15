from rest_framework import serializers

class ResetPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    token = serializers.CharField()
