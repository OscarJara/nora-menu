from rest_framework import serializers

from .models import (
    Menu,
    Option
)

class OptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Option
        fields = ('__all__')
        
class MenuSerializer(serializers.ModelSerializer):
        
    options = OptionSerializer(many=True)
    
    class Meta:
        model = Menu
        fields = (
            'date',
            'options'
        )