import os
import json
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(join(dirname(__file__), '.env'))

from slacker import Slacker

class Slack:
    
    '''
        This class is intended to be instantiated and generate an integration with slack, which uses the slacker library
        
        Example of how to use:
        
            slack = Slack()
            slack.message(
                message='message test',
                channel='#general'
            )
    '''
    def __init__(self):
        
        # the variable is imported from .env file
        self.slack_token = os.getenv("BOT_SLACK_TOKEN","")
        
        # a slacker object is instantiated from the imported token
        self.slack = Slacker(self.slack_token)
        
    def message(self,message,channel):
        
        '''
            this method is in charge of sending the message to a slack channel.
            
            Parameters:
            
                message: string (message to be sent to the slack channel)
                channel: string (channel that the message will be sent)
                
            Example Correct Response:
        
                code: 200
                response:     
                    {
                        "ok":true,
                        "channel":"C01AZ56NAKB",
                        "ts":"1600053020.000800",
                        "message":{
                            "type":"message",
                            "subtype":"bot_message",
                            "text":"message of test",
                            "ts":"1600053020.000800",
                            "username":"bot",
                            "bot_id":"B01AZ58NWC9"
                        }
                    }
                    
            Example Incorrect Response:
            
                Example 1:
                
                    message empty.
                    
                    code: 400
                    response: 'the message cannot be empty'
                    
                Example 2:
                
                    channel empty.
                    
                    code: 400
                    response: 'the channel cannot be empty'
                    
                Example 3:
                
                    channel wrong.
                    
                    code: 400
                    response: 'channel_not_found'
        '''
        
        try:
            # validation that message is not empty
            if not message:
                return 400, {
                    'error':'the message cannot be empty'
                }
            
            # validation that channel is not empty
            if not channel:
                return 400,{
                    'error':'the channel cannot be empty'
                }
            
            # post request to create message
            response = self.slack.chat.post_message(channel,message)
                        
            return 200,response.body

        except Exception as e:
            
            # error handling and code return with eror json
            return 400, {
                'error':str(e)
            }