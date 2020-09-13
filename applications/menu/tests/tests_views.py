from django.test import TestCase

# Create your tests here.

from applications.menu.views import *
from rest_framework.reverse import reverse
from rest_framework import status

from applications.menu.models import (
    Menu,
    Option
)

import datetime

'''

    3. create menu whitout options
    5. create menu with date past
    6. create menu with another user other than the administrator profile
    7. list all menus with a profile other than administrator
    8. list all menus with administrator profile
    9. delete menu with selections
    
    
    12. add menu to celery for to send reminder notifications
    12. test slack notifications
'''

class MenuViewTest(TestCase):
    
    def setUp(self):
        
        option = Option()
        option.description = 'Pure de zapallo con escalopa'
        option.save()
        self.option_id = option.id
        
        menu = Menu()
        menu.date = datetime.date.today()
        menu.save()
                
        self.menu_id = menu.id
    
    def test_menu(self):
        '''
            View menu rendering
        '''
        response = self.client.get('/menus/')
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')

    def test_api_list_menu(self):
        '''
            test by making a request to the listing api for menus, a 301 code is expected
        '''
        response = self.client.get('/API/menus')
        self.assertEqual(response.status_code,status.HTTP_301_MOVED_PERMANENTLY,'the returned code is not what we expected')

class OptionViewTest(TestCase):
    
    def setUp(self):
        
        option = Option()
        option.description = 'Pure de zapallo con escalopa'
        option.save()
        self.option_id = option.id
        
        menu = Menu()
        menu.date = datetime.date.today()
        menu.save()
                
        self.menu_id = menu.id

    def test_create_option(self):
        
        '''
            A new option is created through the add-options view,
            a creation without error is expected, with return code 302
        '''
        payload_test = {
            'description':'Zapallo italiano'
        }
        response = self.client.post('/add-options/',payload_test)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
        
    def test_create_option_empty_fields(self):
            
        '''
            A new option is created through the add-options view,
            a creation with error expected, with return code 200
        '''
        payload_test = {
            'description':''
        }
        response = self.client.post('/add-options/',payload_test)
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
    
    def test_create_option_wrong_fields(self):
            
        '''
            A new option is created through the add-options view,
            a creation with error expected because the fields it's wrongs, with return code 200
        '''
        payload_test = {
            'descripttion':''
        }
        response = self.client.post('/add-options/',payload_test)
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
        
    def test_list_options(self):
        '''
            view listing and rendering is tested
        '''
        response = self.client.get('/options/')
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')