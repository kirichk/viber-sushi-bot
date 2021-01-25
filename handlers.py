"""
Separate file for handling user messages.

Contains all bot answers for ViberMessageRequest
"""
import os
import json
import logging
import utils.resources.keyboards_content as kb
import utils.resources.rich_media_content as rm
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.contact_message import ContactMessage
from viberbot.api.messages.location_message import LocationMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from utils.tools import get_address, dotenv_definer

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

dotenv_definer()

ADMIN = os.getenv("ADMIN")  # Person's ID who will receive all orders


def user_message_handler(viber, viber_request):
    """Receiving a message from user and sending replies."""
    message = viber_request.message
    tracking_data = message.tracking_data
    # Data for usual TextMessage
    reply_text = ''
    reply_keyboard = {}
    # Data for RichMediaMessage
    reply_alt_text = ''
    reply_rich_media = {}

    if tracking_data is None:
        tracking_data = {'comment_mode': 'off'}
    else:
        tracking_data = json.loads(tracking_data)

    if isinstance(message, ContactMessage):
        # Handling reply after user shared his contact infromation
        tracking_data['name'] = message.contact.name
        tracking_data['phone'] = message.contact.phone_number
        reply_keyboard = kb.MENU_KEYBOARD
        reply_text = 'Спасибо! Выберите интересующую Вас категорию.'
    elif isinstance(message, LocationMessage):
        # Handling reply after a user shared his location and transcribing it
        tracking_data['location'] = get_address(message.location)
        reply_keyboard = kb.FINAL_COMFIRMATION_WITH_COMMENT_KEYBOARD
        reply_text = f"Спасибо! Вы указали:\n{tracking_data['location']}\n\n"\
            "Для подтверждения заказа нажмите Заказать. Если хотите "\
            "добавить комментарий, нажмите соответствующую кнопку."
    else:
        text = viber_request.message.text
        if text == 'sets':
            # Dislpaying carousel of items in sets category
            reply_alt_text = 'Выбор сетов'
            reply_rich_media = rm.RICH_MEDIA_SETS
        elif text == 'rolls':
            # Dislpaying carousel of items in rolls category
            reply_alt_text = 'Выбор роллов'
            reply_rich_media = rm.RICH_MEDIA_ROLLS
        elif text == 'pizza':
            # Dislpaying carousel of items in pizza category
            reply_alt_text = 'Выбор пиццы'
            reply_rich_media = rm.RICH_MEDIA_PIZZA
        elif text == 'snacks':
            # Dislpaying carousel of items in snacks category
            reply_alt_text = 'Выбор закусок'
            reply_rich_media = rm.RICH_MEDIA_SNACKS
        elif text == 'menu':
            # Dislpaying categories of menu
            reply_keyboard = kb.MENU_KEYBOARD
            reply_text = 'Выберите интересующую Вас категорию.'
        elif text == 'confirmation':
            # If user confirmed his order he should send his location
            reply_keyboard = kb.SHARE_LOCATION_KEYBOARD
            reply_text = 'Укажите адрес доставки заказа. '\
                         'Для этого нажмите Отправить Локацию.'
        elif text == 'comment':
            # Setting the possibility to write a comment
            tracking_data['comment_mode'] = 'on'
            reply_text = 'Напишите Ваши пожелания в ответ на это сообщение.'
        elif text[:5] == 'order':
            # Handling user selection of product, and dislpaying his choice
            ordered_item = text.split('-')[1]
            if 'order' in tracking_data:
                tracking_data['order'].append(ordered_item)
            else:
                tracking_data['order'] = [ordered_item]
            reply_text = f'Вы выбрали:\n{", ".join(tracking_data["order"])}\n\n'\
                'Если желаете выбрать что-нибудь еще, нажмите Меню. '\
                'Для продолжения, нажмите Оформить заказ.'
            reply_keyboard = kb.ORDER_COMFIRMATION_KEYBOARD
        elif text == 'send_order':
            # Final step, sends all info to manager and resets tracking_data
            tracking_data['comment_mode'] = 'off'
            mesage_to_admin = f"Новый заказ!\nИмя: {tracking_data['name']}\n"\
                              f"Номер: {tracking_data['phone']}\n"\
                              f"Заказ: {', '.join(tracking_data['order'])}\n"\
                              f"Адрес: {tracking_data['location']}\n"\
                              f"Комментарий: {tracking_data['comment']}\n"
            viber.send_messages(ADMIN, TextMessage(text=mesage_to_admin))
            tracking_data['order'] = []
            tracking_data['location'] = ''
            tracking_data['comment'] = ''
            reply_text = 'Спасибо за заказ, менеджер в скором времени'\
                         ' свяжется с Вами.'
            reply_keyboard = kb.MENU_KEYBOARD
        else:
            # Handling text messages from client and checking if it's a comment
            if tracking_data['comment_mode'] == 'on':
                tracking_data['comment'] = text
                reply_text = 'Спасибо! Для подтверждения заказа нажмите '\
                             'Заказать.'
                reply_keyboard = kb.FINAL_COMFIRMATION_WITHOUT_COMMENT_KEYBOARD
            else:
                reply_text = 'Воспользуйтесь клавиатурой с внопками для '\
                             'управления ботом.'
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
