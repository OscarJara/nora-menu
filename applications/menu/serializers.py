from rest_framework import serializers

from .models import (
    Menu,
    Option
)

class OptionSerializer(serializers.ModelSerializer):
    '''
        Base serializer of the option model.
    '''
    class Meta:
        model = Option
        fields = ('__all__')
        
class MenuSerializer(serializers.ModelSerializer):
    '''
        base serializer for the menus, a field is added that is not required, but will be used by another serializer for menu selection.
        
        Use the option serializer to generate the relation.
    '''  
    options = OptionSerializer(many=True)
    user_id = serializers.IntegerField(required=False)
    class Meta:
        model = Menu
        fields = (
            'id',
            'date',
            'options',
            'user_id',
        )
        

class SpecificMenuSerializer(serializers.ModelSerializer):
        
    options = OptionSerializer(many=True)
    user_id = serializers.SerializerMethodField('get_user_id')
    
    class Meta:
        model = Menu
        fields = (
            'id',
            'date',
            'options',
            'user_id'
        )
        
    def get_user_id(self,obj):
        
        user_id = self.context.get('user')
        if user_id:
            return user_id
