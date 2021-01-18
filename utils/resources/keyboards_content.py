"""Keyboards for Viber bot messages."""


MENU_NAMES = [
    ('sets', 'Сеты'),
    ('rolls', 'Роллы'),
    ('pizza', 'Пицца'),
    ('snacks', 'Закуски')
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


MENU_KEYBOARD = {
    "DefaultHeight": False,
    "BgColor": "#FFFFFF",
    "Type": "keyboard",
    "Buttons": [{
            "Columns": 3,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": item[0],
            "ReplyType": "message",
            "Text": item[1]
        } for item in MENU_NAMES]
}
