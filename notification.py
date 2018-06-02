'''
    This is the Notification class file
    Copyright (C) <2018>  <Ali Ba Wazir>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
