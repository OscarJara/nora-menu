from django import forms

from .models import (
    Option,
    Menu
)

import datetime

class BaseOptionForm(forms.ModelForm):
    
    '''
        Base form class for Option.
        
        the fields are customized:
        
            * description : configure a textInput and add placeholder
    '''
    class Meta:
        model = Option
        fields = ['description']
        widgets = {
            'description':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese descripción del plato'
                }
            )
        }
        
        
    def clean_description(self):
        '''
            validate that the description does not come empty
        '''
        if not self.cleaned_data['description']:
            raise forms.ValidationError('Debe ingresar una descripción para el plato, no puede estar vacio')
        return self.cleaned_data['description']

class BaseMenuForm(forms.ModelForm):
    '''
        Base form class for Menu.
        
        The fields are customized:
        
            * date : type DateField, the restriction is, the date can be before today
            * options : type Select, it will list all available menu options
    '''

    class Meta:
        model = Menu
        fields = (
            'date', 
            'options',
        )
        widgets = {
            'date':forms.DateInput(
                format='%d-%m-%Y'
            ),
            'options':forms.SelectMultiple()
        }