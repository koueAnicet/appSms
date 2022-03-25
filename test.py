# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from dotenv import load_dotenv

def send_text_message(destination: str, message: str):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                body='Hi there',
                                from_='+15017122661',
                                to=+2250566538168
                            )

    print(message.sid)

def main():
    send_text_message("+2250566538168","bonjour se suis anicet!")

if __name__=="__name__":
    main()
