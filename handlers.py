"""
Separate file for handling user messages.

Contains all bot answers for ViberMessageRequest
"""
import json
import logging
import utils.resources.keyboards_content as kb
import utils.resources.rich_media_content as rm
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.contact_message import ContactMessage
from viberbot.api.messages.location_message import LocationMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from utils.tools import get_address

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def user_message_handler(viber, viber_request):
    """Receiving a message from user and sending replies."""
    message = viber_request.message
    print(message)
    tracking_data = message.tracking_data
    # Data for usual TextMessage
    reply_text = ''
    reply_keyboard = {}
    # Data for RichMediaMessage
    reply_alt_text = ''
    reply_rich_media = {}

    if tracking_data is None:
        tracking_data = {}
    else:
        tracking_data = json.loads(tracking_data)

    if isinstance(message, ContactMessage):
        tracking_data['name'] = message.contact.name
        tracking_data['phone'] = message.contact.phone_number
        reply_keyboard = kb.MENU_KEYBOARD
        reply_text = 'Спасибо! Выберите интересующую Вас категорию.'
    elif isinstance(message, LocationMessage):
        tracking_data['location'] = get_address(message.location)
        reply_text = f"{tracking_data['location']}"
    else:
        text = viber_request.message.text
        if text == 'sets':
            reply_alt_text = 'Выбор сетов'
            reply_rich_media = rm.RICH_MEDIA_SETS
        elif text == 'rolls':
            reply_alt_text = 'Выбор роллов'
            reply_rich_media = rm.RICH_MEDIA_ROLLS
        elif text == 'pizza':
            reply_alt_text = 'Выбор пиццы'
            reply_rich_media = rm.RICH_MEDIA_PIZZA
        elif text == 'snacks':
            reply_alt_text = 'Выбор закусок'
            reply_rich_media = rm.RICH_MEDIA_SNACKS
        elif text[:5] == 'order':
            ordered_item = text.split('-')[1]
            reply_text = ordered_item
        else:
            reply_text = 'Ну Привет'
    logger.info(tracking_data)
    tracking_data = json.dumps(tracking_data)

    if reply_rich_media:
        reply = [RichMediaMessage(rich_media=reply_rich_media,
                                  alt_text=reply_alt_text,
                                  tracking_data=tracking_data,
                                  min_api_version=7)]
    else:
        reply = [TextMessage(text=reply_text,
                             keyboard=reply_keyboard,
                             tracking_data=tracking_data,
                             min_api_version=3)]
    viber.send_messages(viber_request.sender.id, reply)
