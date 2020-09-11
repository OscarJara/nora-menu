from django.test import TestCase
from rest_framework.reverse import reverse

from applications.users.models import User

# Create your tests here.

'''
    7. list users with a profile other than administrator
    8. with user select valid menu
    9. with user select invalid menu
    10. with user select 2 menus in the same date
'''

class UserViewTest(TestCase):
    
    def setUp(self):
        new_user = User()
        new_user.full_name = 'testUser1'
        new_user.mail = 'test@test.cl'
        new_user.password = 'UserTest01'
        new_user.profile = 1
        new_user.save()
        self.user_id = new_user.id
        
    def test_create_user(self):
        payload_test = {
            "full_name": "testUser2",
            "mail": "test@test.cl",
            "password": "UserTest01",
            "profile": 1
        }
        response = self.client.post('/add-user/',payload_test)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
        
    def test_create_user_emptyFields(self):
        payload_test = {
            "full_name": "",
            "mail": "",
            "password": "",
            "profile": 5
        }
        response = self.client.post('/add-user/',payload_test)
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
        
    def test_create_user_incorrectData(self):
        payload_test = {
            "full_name": 22211,
            "mail": "",
            "password": ""
        }
        response = self.client.post('/add-user/',payload_test)
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
        
    def test_list_users(self):
        response = self.client.get(reverse('user_app:home'))
        self.assertEqual(response.status_code,200,'the returned code is not what we expected')
        
    def test_update_user(self):
        
        payload_update_test = {
            "full_name": "UserTest1",
            "mail": "test@test.cl",
            "password": "UserTest012",
            "profile": 0
        }
        
        url_update = '/update-user/%s' %(str(self.user_id))
        response = self.client.post(url_update,payload_update_test)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
    
    def test_delete_user(self):
        
        url_delete = '/delete-user/%s' %(str(self.user_id))
        response = self.client.post(url_delete)
        self.assertEqual(response.status_code,302,'the returned code is not what we expected')
    
    # 