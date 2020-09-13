from django import forms

from .models import (
    Option,
    Menu
)

import pytz
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
        
            * date : type DateInput, the restriction is, the date can be before today
            * options : type Select, it will list all available menu options
    '''

    class Meta:
        model = Menu
        fields = (
            'date', 
            'options',
        )
        widgets = {
            'options':forms.SelectMultiple()
        }
        
    def clean_date(self):
        
        '''
            clean_date verifies that the date to create a menu is not less than the current date, so as not to create menus that cannot be selected.
        '''
        if self.cleaned_data['date'] < datetime.date.today():
            raise forms.ValidationError('La fecha ingresada para crear el menu no puede ser para una anterior a la de hoy')
        
        return self.cleaned_data['date']