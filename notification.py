#######################################################################
#   notification.py
#   This is the Notification class file
#   Written by: Ali Ba Wazir, May 2018
#######################################################################
from twilio.rest import Client

class Notification():

    def __init__(self, content):
        if content is None or type(content) is not str:
            raise ValueError('invalid argument: content')
        self.content = content

    def send_text_message(self, phone_num):
        # use twilio to send the message
        account_sid = 'AC94ec1f1ab4fd2648255e332d1cd6de10'
        auth_token = '40990ce285de657752ab45091558c00f'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = self.content,
            to = phone_num,
            from_ = '+18737386267'
        )
        print message.sid
