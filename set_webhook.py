import requests
import json


# Setting up webhook parameters
auth_token = '4c82beadd5000d6f-9c279d60da57302f-7f837b53210f082f'
hook = 'https://chatapi.viber.com/pa/set_webhook'
headers = {'X-Viber-Auth-Token': auth_token}
body = dict(url='https://80aa9f7388ee.ngrok.io',
            event_types=['unsubscribed',
                         'conversation_started',
                         'message',
                         'seen',
                         'delivered'])

# Sending POST request to apply a webhook, and printing results
r = requests.post(hook, json.dumps(body), headers=headers)
print(r.json())
