"""Scipt for setting a webhook for a Viber bot."""
import os
import requests
import json
from dotenv import load_dotenv

# Loading Environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Setting up webhook parameters
auth_token = os.getenv("TOKEN")
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}
body = dict(url='https://viber-sushi-bot.herokuapp.com/',
            event_types=['unsubscribed',
                         'conversation_started',
                         'message',
                         'seen',
                         'delivered'])

# Sending POST request to apply a webhook, and printing results
r = requests.post(hook, json.dumps(body), headers=headers)
print(r.json())
