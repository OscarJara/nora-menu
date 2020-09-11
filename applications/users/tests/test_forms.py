from django.test import TestCase

from applications.users.forms import BaseUserForm

class CreateUserFormTest(TestCase):
   
    def test_UserForm(self):
        '''
            In this test a correct form is generated,
            the error response must be empty
        '''
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
        '''
            the full_name must come with an error,
            since the BaseUserForm expects a longer name than 5 characters
        '''
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
        '''
            the password must come with an error,
            since the BaseUserForm expects a longer password than 8 characters
        '''
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
        '''
            the password must come with an error,
            since password is a required field
        '''
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
        '''
            The mail must come with an error,
            since the format is validated from BaseUserForm through a regular expression
        '''
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