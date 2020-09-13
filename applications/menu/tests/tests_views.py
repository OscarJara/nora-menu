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

    7. list all menus with a profile other than administrator
    8. list all menus with administrator profile
        
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

    def test_api_specific_menu_wrong_url(self):
        '''
            A request is made looking for a specific menu, but with the wrong url, a 404 code is expected since the url does not exist
        '''
        url = '/API/specific_menu?menu=%s' % (self.menu_id)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND,'the returned code is not what we expected')
    
    def test_api_specific_menu(self):
        '''
            request is made looking for a specific menu with the correct url
        '''
        url = '/API/specific?menu=%s' % (self.menu_id)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_301_MOVED_PERMANENTLY,'the returned code is not what we expected')
        
    def test_create_menu(self):
        '''
            request post to add-menu, create a new menu.
        '''
        payload_test = {
            'date':datetime.date.today(),
            'option':self.option_id
        }
        response = self.client.post('/add-menu/',payload_test)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')

    def test_create_menu_date_past(self):
        '''
            request post to add-menu, create a new menu with date past.
        '''
        previous_date = datetime.date.today() - datetime.timedelta(days=1)
        payload_test = {
            'date':previous_date,
            'option':self.option_id
        }
        response = self.client.post('/add-menu/',payload_test)
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
        
    def test_update_menu(self):
        '''
            request post to update-menu, modify a menu created in SetUp, no errors are expected
        '''
        payload_test = {
            'id':str(self.menu_id),
            'date':datetime.date.today(),
            'option':self.option_id
        }
        url = '/update-menu/%s' % (str(self.menu_id))
        response = self.client.post(url,payload_test)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
        
    def test_delete_menu(self):
        '''
            request post to delete-menu, delete a menu created in SetUp, no errors are expected.
        '''
        url = '/delete-menu/%s' % (str(self.menu_id))
        response = self.client.post(url)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
        
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