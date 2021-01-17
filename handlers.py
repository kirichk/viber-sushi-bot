"""
Separate file for handling user messages.

Contains all bot answers for ViberMessageRequest
"""

import json
import logging
import requests
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.url_message import URLMessage


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def user_message_handler(viber, viber_request):
    message = viber_request.message.text
    viber.send_messages(viber_request.sender.id, message)
