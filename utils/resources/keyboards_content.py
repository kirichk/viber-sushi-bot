"""Keyboards for Viber bot messages."""
from ..tools import keyboard_consctructor


MENU_NAMES = [
    ('sets_rolls', 'Сеты и Роллы'),
    ('guncans_sushi', 'Гунканы и Суши'),
    ('pizza_snacks', 'Пицца и Закуски'),
    ('other', 'Ещё')
]

SETS_ROLLS_MENU = [
    ('sets', 'Сеты'),
    ('rolls', 'Роллы')
]

GUNCANS_SUSHI_MENU = [
    ('guncans', 'Гунканы'),
    ('sushi', 'Суши')
]

PIZZA_SNACKS_MENU = [
    ('pizza', 'Пицца'),
    ('combo', 'Комбо'),
    ('nuggets_wings', 'Наггетсы и Крылышки'),
    ('mussils', 'Мидии')
]

OTHER_MENU = [
    ('sauces', 'Соусы'),
    ('drinks', 'Напитки'),
    ('offers', 'Акции'),
    ('delivery', 'Доставка')
]

SHARE_PHONE_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "share-phone",
            "ActionBody": "phone_reply",
            "ReplyType": "message",
            "Text": "Поделиться номером"
        }
    ]
}

DELIVERY_TYPE_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "pickup",
            "ReplyType": "message",
            "Text": "Самовывоз"
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "address",
            "ReplyType": "message",
            "Text": "Доставка"
        }
    ]
}

SHARE_LOCATION_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "location-picker",
            "ActionBody": "location",
            "ReplyType": "message",
            "Text": "Отправить локацию"
        }
    ]
}

ORDER_COMFIRMATION_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "menu",
            "ReplyType": "message",
            "Text": "Меню"
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "confirmation",
            "ReplyType": "message",
            "Text": "Оформить заказ"
        }
    ]
}

GO_TO_MENU_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "menu",
            "ReplyType": "message",
            "Text": "Меню"
        }
    ]
}

FINAL_COMFIRMATION_WITH_COMMENT_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "send_order",
            "ReplyType": "message",
            "Text": "Заказать"
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "comment",
            "ReplyType": "message",
            "Text": "Добавить комментарий"
        }
    ]
}

FINAL_COMFIRMATION_WITHOUT_COMMENT_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 6,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "send_order",
            "ReplyType": "message",
            "Text": "Заказать"
        }
    ]
}

ORDER_BUTTON = [
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "confirmation",
            "ReplyType": "message",
            "Text": "Изменить заказ"
        },
        {
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "confirmation",
            "ReplyType": "message",
            "Text": "Оформить заказ"
        },
]

MENU_BUTTON = {
    "Columns": 6,
    "Rows": 1,
    "BgColor": "#e6f5ff",
    "BgLoop": True,
    "ActionType": "reply",
    "ActionBody": "menu",
    "ReplyType": "message",
    "Text": "Меню"
}

MENU_KEYBOARD = keyboard_consctructor(MENU_NAMES)
SETS_ROLLS_KEYBOARD = keyboard_consctructor(SETS_ROLLS_MENU)
GUNCANS_SUSHI_KEYBOARD = keyboard_consctructor(GUNCANS_SUSHI_MENU)
PIZZA_SNACKS_KEYBOARD = keyboard_consctructor(PIZZA_SNACKS_MENU)
OTHER_KEYBOARD = keyboard_consctructor(OTHER_MENU)
