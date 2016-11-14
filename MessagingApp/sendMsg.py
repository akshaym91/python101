from twilio import rest

account_sid = "ACdbddb22a5c0d5942e423a4b8b67d7b8c" # Your Account SID from www.twilio.com/console
auth_token  = "0bd8d9660b8d0088744fa5515d3534a9"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token, "https://api.twilio.com:8443")

message = client.messages.create(body="Hi Mithun! Are you a fullstack developer looking for a change? Please leave a message with YES-MITHUN or give a missed call at +917829392496. We offer $30 per hour.",
    to="+917829392496",    # Replace with your phone number only 
    from_="+12135998443") # Replace with your Twilio number

print(message.sid)