from rest_framework import serializers

from .models import (
    UserMenu,
    User
)

from applications.menu.models import Option
from applications.menu.serializers import OptionSerializer


class UserAuth(serializers.ModelSerializer):
    '''
        serializer to simulate a login from an email, it will return specific data which defines if all the menus will be listed or only the worker's
    '''
    class Meta:
        model = User
        fields = (
            'id',
            'mail', 
            'profile'
        )
        
class UserSerializer(serializers.ModelSerializer):
    '''
        base serializer of a user, where it will return all the fields
    '''
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
            'date',
        )
        
    def get_option_select(self,obj):
        
        option = Option.objects.filter(id=obj.option).values('description')
        option = option[0]['description']
        return option