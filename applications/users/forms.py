from django import forms

from .models import User, UserMenu

import re

class CreateUser(forms.ModelForm):
    
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
        
        mail = self.cleaned_data['mail']
        validate_mail = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",mail)
        if not validate_mail:
            raise forms.ValidationError('Ingrese un email valido.')
        
        return mail