"""Keyboards for Viber bot messages."""


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
