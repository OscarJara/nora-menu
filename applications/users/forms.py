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
            'password': forms.PasswordInput(),
            'mail':forms.EmailInput(),
        }
        
        
    def clean_mail(self):
        
        mail = self.cleaned_data['mail']
        validate_mail = re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",mail)
        if not validate_mail:
            raise forms.ValidationError('Ingrese un email valido.')
        
        return mail