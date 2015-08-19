from twilio.rest import TwilioRestClient
import os
 
account_sid = os.environ['TWILIO_ACCOUNT'] #replace with your twilio account number
auth_token  = os.environ['TWILIO_API_KEY'] #replace with your twilio auth token
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is a test message! Hello.",
    to = os.environ["CELL_PHONE_NUMBER"], # Replace with your phone number
    from_ = os.environ["TWILIO_PHONE_NUMBER"]) # Replace with your Twilio number

print message.sid