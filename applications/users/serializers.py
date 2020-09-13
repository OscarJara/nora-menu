from rest_framework import serializers

from .models import (
    UserMenu
)

class UserMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserMenu
        fields = (
            'user',
            'menu',
            'option',
            'observation'
        )