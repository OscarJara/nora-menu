from django.test import TestCase

from applications.users.forms import BaseUserForm

class CreateUserFormTest(TestCase):
   
    def test_UserForm(self):
        form = BaseUserForm(
            data={
                'full_name':'UserTestForm',
                'mail':'mailtest@example.com',
                'password':'testestest',
                'profile':1
            }
        )
        self.assertEqual(
            form.errors,
            {},
            'unexpected error response'
        ) 
    
    def test_short_fullName(self):
        form = BaseUserForm(
            data={
                'full_name':'user',
                'mail':'mailtest@example.com',
                'password':'testp',
                'profile':1
            }
        )
        self.assertEqual(
            form.errors['full_name'],
            ['Ingrese un nombre más largo'],
            'unexpected error response'
        )
    def test_short_password(self):
        form = BaseUserForm(
            data={
                'full_name':'UserTestForm',
                'mail':'mailtest@example.com',
                'password':'testp',
                'profile':1
            }
        )
        self.assertEqual(
            form.errors['password'],
            ['La contraseña debe tener un largo minimo de 8'],
            'unexpected error response'
        )
    
    def test_password_withoutNumber(self):
        form = BaseUserForm(
            data={
                'full_name':'UserTestForm',
                'mail':'mailtest@example.com',
                'password':'',
                'profile':1
            }
        )
        self.assertEqual(
            form.errors['password'],
            ['This field is required.'],
            'unexpected error response'
        )
    
    def test_mail_withoutFormat(self):
        form = BaseUserForm(
            data={
                'full_name':'UserTestForm',
                'mail':'mailtest@com',
                'password':'PasswordTest',
                'profile':1
            }
        )
        self.assertEqual(
            form.errors['mail'],
            ['Enter a valid email address.'],
            'unexpected error response'
        )