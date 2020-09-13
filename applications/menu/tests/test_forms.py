from django.test import TestCase

from applications.menu.forms import (
    BaseOptionForm,
    BaseMenuForm
)

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