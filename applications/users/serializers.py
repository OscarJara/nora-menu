from rest_framework import serializers

from .models import (
    UserMenu,
    User
)

from applications.menu.models import Option
from applications.menu.serializers import OptionSerializer


class UserAuth(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'mail', 
            'profile'
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        
class UserMenuSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    option_select = serializers.SerializerMethodField()
    class Meta:
        model = UserMenu
        
        fields = (
            'user',
            'menu',
            'option',
            'observation',
            'option_select',
        )
        
    def get_option_select(self,obj):
        
        option = Option.objects.filter(id=obj.option).values('description')
        option = option[0]['description']
        return option