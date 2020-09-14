from django.test import TestCase

from .slack import Slack
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

    def test_create_message_Channel_empty(self):
        
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