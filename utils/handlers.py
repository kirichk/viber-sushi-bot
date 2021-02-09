"""
Separate file for handling user messages.

Contains all bot answers for ViberMessageRequest
"""
import os
import json
import logging
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.contact_message import ContactMessage
from viberbot.api.messages.location_message import LocationMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from .resources import keyboards_content as kb
from .tools import get_address, dotenv_definer
from .response_map import RICH_RESPONSE_MAP, KEYBOARD_RESPONSE_MAP


dotenv_definer()
ADMINS = os.getenv("ADMIN").split('-')  # Person's ID who will receive all orders

logger = logging.getLogger()
logger.setLevel(os.getenv("LOG_LEVEL"))


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
        #####
        user_data = f'{viber_request.sender.id} - {message.contact.phone_number}'
        feedback = TextMessage(text=user_data)
        viber.send_messages(ADMIN, feedback)
        #####
    elif isinstance(message, LocationMessage):
        # Handling reply after a user shared his location and transcribing it
        tracking_data['location'] = get_address(message.location)
        reply_keyboard = kb.FINAL_COMFIRMATION_WITH_COMMENT_KEYBOARD
        reply_text = f"Спасибо! Вы указали:\n{tracking_data['location']}\n\n"\
            "Для подтверждения заказа нажмите Заказать. Если хотите "\
            "добавить комментарий, нажмите соответствующую кнопку."
    else:
        text = viber_request.message.text

        ##########################################################
        ######## Dislpaying keyboard of different items ##########
        ##########################################################

        if text in KEYBOARD_RESPONSE_MAP:
            reply_text = KEYBOARD_RESPONSE_MAP[text][0]
            reply_keyboard = KEYBOARD_RESPONSE_MAP[text][1]
            without_menu_button_list = ['menu', 'confirmation',
                                        'offers', 'delivery']
            if len(tracking_data['order']) > 0 and text not in ['address','confirmation']:
                if kb.ORDER_BUTTON[0] not in reply_keyboard['Buttons']:
                    reply_keyboard['Buttons'] += kb.ORDER_BUTTON
            if kb.MENU_BUTTON not in reply_keyboard['Buttons'] and text not in without_menu_button_list:
                reply_keyboard['Buttons'].append(kb.MENU_BUTTON)
        ##########################################################
        ######## Dislpaying carousel of different items ##########
        ##########################################################

        elif text in RICH_RESPONSE_MAP:
            reply_alt_text = RICH_RESPONSE_MAP[text][0]
            reply_rich_media = RICH_RESPONSE_MAP[text][1]

        ##########################################################

        elif text == 'pickup':
            tracking_data['location'] = 'Самовывоз'
            reply_text = "Для подтверждения заказа нажмите Заказать. Если хотите "\
                         "добавить комментарий, нажмите соответствующую кнопку."
            reply_keyboard = kb.FINAL_COMFIRMATION_WITH_COMMENT_KEYBOARD
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
            mesage_to_admin = "Новый заказ!\n"
            if tracking_data['name'] is not None:
                mesage_to_admin += f"Имя: {tracking_data['name']}\n"
            mesage_to_admin += f"Номер: {tracking_data['phone']}\n"\
                               f"Заказ: {', '.join(tracking_data['order'])}\n"\
                               f"Адрес: {tracking_data['location']}\n"
            if 'comment' in tracking_data:
                mesage_to_admin += f"Комментарий: {tracking_data['comment']}\n"
            for admin in ADMINS:
                viber.send_messages(admin, TextMessage(text=mesage_to_admin))
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
                if 'phone' in tracking_data:
                    reply_keyboard = kb.MENU_KEYBOARD
                else:
                    reply_keyboard = kb.SHARE_PHONE_KEYBOARD

    logger.info(tracking_data)
    tracking_data = json.dumps(tracking_data)

    if reply_rich_media:
        reply = []
        reply_text = 'Выберите желаемую позицию из перечня выше. Для '\
                     'возвращения в меню воспользуйтесь клавиатурой внизу.'
        for template in reply_rich_media:
            reply.append(
                RichMediaMessage(rich_media=template,
                                 alt_text=reply_alt_text,
                                 tracking_data=tracking_data,
                                 min_api_version=7)
                )
        reply.append(
            TextMessage(text=reply_text,
                                 keyboard=kb.GO_TO_MENU_KEYBOARD,
                                 tracking_data=tracking_data,
                                 min_api_version=3)
        )
    else:
        reply = [TextMessage(text=reply_text,
                             keyboard=reply_keyboard,
                             tracking_data=tracking_data,
                             min_api_version=3)]
    viber.send_messages(viber_request.sender.id, reply)