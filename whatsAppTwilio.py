# Download the helper library from https://www.twilio.com/docs/python/install
from decouple import config
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config('TWILIO_ACCOUNT_SID', default='SID')
auth_token = config('TWILIO_AUTH_TOKEN', default='TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    body='¡Hola! Soy s-manuel, Tu acesor diguital. ¿Cómo puedo ayudarte?',
    from_=config('WHATSAPP_FROM', default='FROM'),
    to=config('WHATSAPP_TO', default='TO')
)

print(message.sid)
