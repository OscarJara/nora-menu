from django import forms

from .models import User, UserMenu

import re

class BaseUserForm(forms.ModelForm):
    
    '''
        Base form class for User.
        
        the fields are customized:
        
            * full_name : configure a textInput and add placeholder
            * mail : configure a EmailInput and add placeholder
            * password : configure PasswordInput and add placeholder
            * profile : configure Select and add placeholder
    '''
    class Meta:
        model = User
        fields = (
            'full_name',
            'mail',
            'password',
            'profile'
        )
        widgets = {
            'full_name':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombre completo'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder':'Ingrese contraseña para el usuario'
                }
            ),
            'mail':forms.EmailInput(
                attrs={
                    'placeholder':'Ingrese email del usuario'
                }
            ),
            
            'profile':forms.Select(
                attrs={
                    'placeholder':'Ingrese perfil'
                }
            )
        }
        
        
    def clean_mail(self):
        '''
            mail is validated through a regular expression.
            if not matched returns error
        '''
        mail = self.cleaned_data['mail']
        validate_mail = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",mail)
        if not validate_mail:
            raise forms.ValidationError('El email debe ser valido')
        
        return mail
    
    def clean_full_name(self):
        '''
            the number of characters of full_name is validated.
            if not matched returns error
        '''
        full_name = self.cleaned_data['full_name']
        if len(full_name) <5:
            raise forms.ValidationError('Ingrese un nombre más largo')
        return full_name
    
    def clean_password(self):
        '''
            the number of characters of password is validated.
            if not matched returns error
        '''
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError('La contraseña debe tener un largo minimo de 8')        
        return password