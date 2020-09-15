from django.test import TestCase

from .slack import Slack
from .celery.task import send_reminder

import uuid

class SlackTest(TestCase):

    def setUp(self):
        self.slack = Slack()
        
    def test_create_message(self):
        
        input_message = 'message of test'
        code,response = self.slack.message(
            message=input_message,
            channel='#general'
        )
        
        self.assertEqual(
            code,
            200,
            'the returned code is not what we expected'
        )
        self.assertEqual(
            response['ok'],
            True,
            'unexpected reply message'
        )
        self.assertEqual(
            response['message']['subtype'],
            'bot_message',
            'unexpected reply message'
            )
        self.assertEqual(
            response['message']['text'],
            input_message,
            'unexpected reply message'
            )
        
    def test_create_message_empty(self):
        
        input_message = ''
        code,response = self.slack.message(
            message=input_message,
            channel='general'
        )
        
        self.assertEqual(
            code, 
            400,
            'the returned code is not what we expected'
        )
        self.assertEqual(
            response['error'],
            'the message cannot be empty',
            'unexpected error message'
        )

    def test_create_message_Channel_empty(self):
        
        input_message = 'message of test'
        code,response = self.slack.message(
            message=input_message,
            channel=''
        )
        
        self.assertEqual(
            code, 
            400,
            'the returned code is not what we expected'
        )
        self.assertEqual(
            response['error'],
            'the channel cannot be empty',
            'unexpected error message'
        )

    def test_create_message_Channel_wrong(self):
        
        input_message = 'message of test'
        code,response = self.slack.message(
            message=input_message,
            channel='#notExist'
        )

        self.assertEqual(
            code, 
            400,
            'the returned code is not what we expected'
        )
        self.assertEqual(
            response['error'],
            'channel_not_found',
            'unexpected error message'
        )
        
    def test_send_reminder(self):
        '''
            test send reminder to slack.
            
            the message is added to an asynchronous task generated with celery, to later send the message to slack.
            
            the url and uuid is generated and created hard as it is just a test message.
            
            response code and message are evaluated.
        '''
        uuidTest = str(uuid.uuid4())
        url = 'https://nora.cornershop.io/menu/%s' %(uuidTest)

        message = 'enter the following url %s' % (url)

        response = send_reminder(
            message=message,
            channel = '#general'
        )
        self.assertEqual(
            response[0],
            200,
            'the returned code is not what we expected'  
        )

        self.assertEqual(
            response[1],
            'ok',
            'unexpected error message'
        )