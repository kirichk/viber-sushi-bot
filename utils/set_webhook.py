"""Scipt for setting a webhook for a Viber bot."""
import os
import requests
import json
from dotenv import load_dotenv

# Loading Environment variables
dotenv_path = os.path.join(__location__, '.env')
load_dotenv(dotenv_path)

URL = os.getenv('URL')

# Setting up webhook parameters
auth_token = os.getenv("TOKEN")
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}
body = dict(url=URL,
            event_types=['unsubscribed',
                         'conversation_started',
                         'message',
                         'seen',
                         'delivered'])

# Sending POST request to apply a webhook, and printing results
r = requests.post(hook, json.dumps(body), headers=headers)
print(r.json())
