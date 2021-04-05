"""Main file that launches Flask server."""
import os
import logging
import utils.resources.keyboards_content as kb
import utils.resources.texts as txt
from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import (ViberFailedRequest,
                                         ViberConversationStartedRequest,
                                         ViberMessageRequest,
                                         ViberSubscribedRequest)
from utils.handlers import user_message_handler
from utils.tools import dotenv_definer
from utils.db_func import create_table


# Loading Environment variables
dotenv_definer()

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='FRESHROLLSbot',
    avatar='https://i.ibb.co/SPXsFsp/image.jpg',
    auth_token=os.getenv("TOKEN")
))

logger = logging.getLogger()
logger.setLevel(os.getenv("LOG_LEVEL"))


@app.before_request
def viber_signature_verifier():
    # Verifying connection
    if not viber.verify_signature(
                        request.get_data(),
                        request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)


@app.route('/', methods=['POST'])
def incoming():
    """Catching all requests to bot and defining the request type."""
    create_table()
    viber_request = viber.parse_request(request.get_data())
    # Defining type of the request and replying to it
    if isinstance(viber_request, ViberMessageRequest):
        # Passing any message from user to message handler in handlers.py
        user_message_handler(viber, viber_request)
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.user.id, [
            TextMessage(text="Спасибо за подписку!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}"
                    .format(viber_request))
    elif isinstance(viber_request, ViberConversationStartedRequest):
        # First touch, sending to user keyboard with phone sharing button
        keyboard = kb.SHARE_PHONE_KEYBOARD
        viber.send_messages(viber_request.user.id, [
            TextMessage(
                text=txt.GREETING,
                keyboard=keyboard,
                min_api_version=3)
            ]
        )
    return Response(status=200)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
