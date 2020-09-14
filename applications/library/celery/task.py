from applications.library.celery.celery_ import app
from applications.library.slack import Slack


@app.task
def send_reminder(message,channel='#general'):
    '''
        generates a background task, where it instantiates slack and sends the reminder.
        
        Parameters: 
            * message : Type string.
                message which will be sent to slack
                
            * channel :  Type string.
                channel to which the user's message will be sent

        Example correct response: 
        
            code : 200
            msg  : 'ok'
            
        Example incorrect response:
        
            code : 400
            msg  : 'a mistake'
    '''
    try:
        slc = Slack()
        slc.message(
            message=message,
            channel=channel,
        )

        return 200,'ok'
    except Exception as e:
        
        return 400,str(e)

