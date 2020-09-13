from django.test import TestCase

from applications.menu.forms import (
    BaseOptionForm,
    BaseMenuForm
)
import datetime

class CreateOptionTest(TestCase):
   
    def test_OptionForm(self):
        '''
            In this test a correct form is generated,
            the error response must be empty
        '''
        form = BaseOptionForm(
            data={
                'description':'Zapallo italiano'
            }
        )
        self.assertEqual(
            form.errors,
            {},
            'unexpected error response'
        ) 
    def test_OptionForm_empty(self):
        '''
            In this test a incorrect form is generated,
            the error response must be description
        '''
        form = BaseOptionForm(
            data={
                'description':''
            }
        )
        self.assertEqual(
            form.errors['description'],
            ['This field is required.'],
            'unexpected error response'
        ) 

class CreateMenuTest(TestCase):
    
    def test_MenuForm(self):
        '''
            In this test a incorrect form is generated,
            the error response must be empty
            
            Incorrect option.
        '''
        form = BaseMenuForm(
            data = {
                'date':datetime.date.today(),
                'options':[4]
            }
        )
        self.assertEqual(
            form.errors['options'],
            ['Select a valid choice. 4 is not one of the available choices.'],
            'unexpected error response'
        )
        
    def test_MenuForm(self):
        '''
            In this test a incorrect form is generated,
            the error response must be empty
            
            Empty option.
        '''
        form = BaseMenuForm(
            data = {
                'date':datetime.date.today(),
                'options':''
            }
        )
        self.assertEqual(
            form.errors['options'],
            ['This field is required.'],
            'unexpected error response'
        )
        
    def test_MenuForm(self):
        '''
            In this test a incorrect form is generated,
            the error response must be empty.
            
                * date with previous date
                * Empty option.
        '''
        previous_date = datetime.date.today() - datetime.timedelta(days=1)
        form = BaseMenuForm(
            data = {
                'date':previous_date,
                'options':''
            }
        )
        self.assertEqual(
            form.errors['options'],
            ['This field is required.'],
            'unexpected error response'
        )
        self.assertEqual(
            form.errors['date'],
            ['La fecha ingresada para crear el menu no puede ser para una anterior a la de hoy'],
            'unexpected error response'
        )