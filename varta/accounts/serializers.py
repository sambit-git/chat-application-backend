from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=32)
    
    class Meta:
        model = User
        fields = ['id', 'username']
