"""
Separate file for handling user messages.

Contains all bot answers for ViberMessageRequest
"""
import json
import logging
import utils.keyboards as kb
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.contact_message import ContactMessage
from viberbot.api.messages.location_message import LocationMessage
from utils.tools import get_address

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def user_message_handler(viber, viber_request):
    """Receiving a message from user and sending replies."""
    message = viber_request.message
    tracking_data = message.tracking_data
    reply = []

    if tracking_data is None:
        tracking_data = {}
    else:
        tracking_data = json.loads(tracking_data)

    if isinstance(message, ContactMessage):
        tracking_data['name'] = message.contact.name
        tracking_data['phone'] = message.contact.phone_number
        reply.append(TextMessage(
                        text=f"Имя: {name}\nНомер: {phone}"))
    elif isinstance(message, LocationMessage):
        tracking_data['location'] = get_address(message.location)
        reply.append(TextMessage(
                                text=f"{tracking_data['location']}"))
    else:
        keyboard = kb.SHARE_LOCATION_KEYBOARD
        reply.append(TextMessage(
                text="Укажите пожалуйста куда нужно доставить Ваш заказ "
                     "нажав Отправить локацию.",
                keyboard=keyboard,
                min_api_version=3)
        )
    tracking_data = json.dumps(tracking_data)
    viber.send_messages(viber_request.sender.id, reply)
